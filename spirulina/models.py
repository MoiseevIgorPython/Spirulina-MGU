from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer, Boolean
from flask_login import UserMixin, AnonymousUserMixin
from spirulina import db


class User(db.Model, UserMixin, AnonymousUserMixin):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    username: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)


class Products(db.Model):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(32), nullable=False)
    description: Mapped[str] = mapped_column(String(32), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    photo: Mapped[str] = mapped_column(String, nullable=True, default=None)
