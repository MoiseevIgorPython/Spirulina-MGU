import os

from flask import redirect, session, url_for
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask_sqlalchemy import SQLAlchemy

from .. import app, db
from ..models import Products, User


# Кастомный View для админки с проверкой аутентификации
class AdminModelView(ModelView):
    def is_accessible(self):
        return 'admin_logged_in' in session

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))

class ProductAdmin(ModelView):
    form_extra_fields = {
        'photo': FileUploadField('photo',
            base_path=os.path.join(os.path.dirname(__file__), '../media'),
            allow_overwrite=False)
    }

# Кастомный View для главной страницы админки
class MyAdminIndexView(AdminIndexView):
    def is_accessible(self):
        return 'admin_logged_in' in session

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login_admin'))


admin = Admin(app, name='Admin Panel',
              template_mode='bootstrap3',
              index_view=MyAdminIndexView()
              )

admin.add_view(ProductAdmin(Products, db.session))
admin.add_view(AdminModelView(User, db.session))
