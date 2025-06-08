from sqlalchemy import create_engine, Integer, String, func
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Date
from datetime import date


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(12), nullable=False)
    birthday: Mapped[date] = mapped_column(Date, nullable=False)
    info: Mapped[str] = mapped_column(nullable=False)
