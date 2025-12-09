from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from .models import User


class UserLogin(FlaskForm):
    username = StringField(
        validators=[DataRequired(message='Поле обязательно'),
                    Length(1, 32)])
    password = StringField(
        validators=[DataRequired(message='Поле обязательно'),
                    Length(1, 32)])
    submit = SubmitField()

    def validate_username(self, field):
        if field.data:
            existing = User.query.filter_by(username=field.data).first()
            if not existing:
                raise ValidationError(
                    f'Пользователь {field.data} не зарегистрирован.')


class OrderForm(FlaskForm):
    name = StringField(
        validators=[DataRequired(message='Укажите имя'),
                    Length(1, 32)])
    number = StringField(
        validators=[DataRequired(message='Укажите номер телефона (11 цифр)')])
    email = EmailField()
    submit = SubmitField()

    # def validate_number(self, field):
    #     if field.data:
    #         if len(field.data) != 11 or not field.data.isdigit():
    #             raise ValidationError('Недопустимый номер телефона')
