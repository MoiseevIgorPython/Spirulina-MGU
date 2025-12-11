# Spirulina Sales Flask-app

Каталог продукции БАДов из спирулины, реализованный на Flask.

## Описание проекта

Проект написан с использованием Flask и расширений:

- Flask-Login  
- Flask-Admin  
- Flask-Mail  
- Flask-Migrate  
- SQLAlchemy  
- и другие  

## Быстрый старт

### Клонирование репозитория

```bash
git clone git@github.com:MoiseevIgorPython/Spirulina-MGU.git
```

Создание и активация виртуального окружения

```bash
python3.12 -m venv venv
```

```bash
. venv/bin/activate - Для Linux/MacOS:
```
```bash
. venv/Scripts/activate - Для Windows:
```

Установка зависимостей

```bash
pip install -r requirements.txt
```

В корне проекта создайте файл .env со следующими переменными:

```bash
FLASK_APP=spirulina
FLASK_DEBUG=1

DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=mysecretkey

MAIL_SERVER=smtp.yandex.ru
MAIL_PORT=465
MAIL_USE_TLS=True

MAIL_USERNAME=myemail@yandex.ru
MAIL_PASSWORD=mypassword
RECIPIENT_MAIL=recipient@gmail.com
```

Инициализация базы данных с Flask-Migrate

```bash
flask db init
```

Структура проекта после инициализации

```bash
spirulina/
├── instance/
│   └── db.sqlite3
├── migrations/
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── spirulina/
│   ├── admin/
│   ├── site/
│   ├── media/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   └── settings.py
├── venv/
├── requirements.txt
└── .env
```

Описание маршрутов

```bash
hostname/ - Главная страница
hostname/<int:id> - Страница отдельного товара
hostname/admin/login/ - Вход в административную панель
hostname/about/ - "Страница ""О спирулине"""
```