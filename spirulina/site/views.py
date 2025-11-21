from flask import render_template, send_from_directory
from spirulina import app, db, mail
from ..models import Products
from ..forms import OrderForm
from ..settings import MEDIA
from flask_mail import Message


def send_mail(theme: str, text: str, sender: str, recipients: list):
    try:
        msg = Message(
            subject=theme,
            sender=(sender, app.config['MAIL_USERNAME']),  # исправляем отправителя
            recipients=recipients
        )
        msg.body = text
        mail.send(msg)
        print(f"Письмо отправлено: {theme}")
        return 'Письмо отправлено'
    except Exception as e:
        print(f"Ошибка отправки письма: {e}")
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
                  recipients=['igor.moiseev1990@gmail.com'])
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


@app.route('/<int:id>')
def detail(id):
    form = OrderForm()
    product = Products.query.get(id)
    return render_template('detail.html', product=product, form=form)


@app.route('/image/<dir_name>/<filename>')
def image(dir_name, filename):
    path = f'{MEDIA}' + '/' + dir_name
    return send_from_directory(path, filename)


@app.route('/about')
def about():
    return render_template('about.html')
