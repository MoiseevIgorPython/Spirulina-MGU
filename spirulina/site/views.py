import os

from dotenv import load_dotenv
from flask import render_template, send_from_directory
from flask_mail import Message

from spirulina import app, mail

from ..forms import OrderForm
from ..models import Products
from ..settings import MEDIA

load_dotenv()


def send_mail(theme: str, text: str, sender: str, recipients: list):
    """Функция отправки писем"""
    try:
        msg = Message(
            subject=theme,
            sender=(sender, app.config['MAIL_USERNAME']),
            recipients=recipients
        )
        msg.body = text
        mail.send(msg)
        return 'Письмо отправлено'
    except Exception as e:
        return f'Ошибка отправки: {str(e)}'


@app.route('/', methods=['GET', 'POST'])
def index():
    order_form = OrderForm()
    products = Products.query.all()
    photos = [product.photo for product in products]
    blog_photos_dir = MEDIA / 'blog'
    blog_photos = [f.name for f in blog_photos_dir.iterdir() if f.is_file()]
    if order_form.validate_on_submit():
        name = order_form.name.data
        number = order_form.number.data
        email = order_form.email.data
        send_mail(theme='Новый заказ',
                  text=f'Пользователь {name}; номер {number}; email {email}',
                  sender=name,
                  recipients=[os.getenv('RECIPIENT_MAIL')])
        return render_template('list.html',
                               products=products,
                               photos=photos,
                               blog_photos=blog_photos,
                               form=OrderForm())
    return render_template('list.html',
                           products=products,
                           photos=photos,
                           blog_photos=blog_photos,
                           form=order_form)


@app.route('/<int:id>', methods=['GET', 'POST'])
def detail(id):
    order_form = OrderForm()
    product = Products.query.get(id)
    if order_form.validate_on_submit():
        name = order_form.name.data
        number = order_form.number.data
        email = order_form.email.data
        send_mail(theme='Новый заказ',
                  text=f'Пользователь {name}; номер {number}; email {email}',
                  sender=name,
                  recipients=[os.getenv('RECIPIENT_MAIL')])
        return render_template('detail.html',
                               product=product,
                               form=OrderForm())
    return render_template('detail.html', product=product, form=order_form)


@app.route('/image/<dir_name>/<filename>')
def image(dir_name, filename):
    path = f'{MEDIA}' + '/' + dir_name
    return send_from_directory(path, filename)


@app.route('/about')
def about():
    return render_template('about.html')
