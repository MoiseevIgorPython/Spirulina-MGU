from flask import request, session, redirect, url_for, render_template
from werkzeug.security import check_password_hash
from ..models import User
from ..forms import UserLogin
from spirulina import app, db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route('/admin/login', methods=['GET', 'POST'])
def login_admin():
    form = UserLogin()
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password) and user.is_admin:
            session['admin_logged_in'] = True
            session['admin_user_id'] = user.id
            return redirect(url_for('admin.index'))
        else:
            return "Неверные учетные данные или недостаточно прав", 401
    return render_template('admin/login.html', form=form)


@app.route('/admin/logout')
def logout_admin():
    session.pop('admin_logged_in', None)
    session.pop('admin_user_id', None)
    return redirect(url_for('login_admin'))
