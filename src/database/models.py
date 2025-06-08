from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), unique=True, index=True, nullable=False)
    phone_number = Column(String(20), unique=True, nullable=False)
    birthday = Column(Date, nullable=False)
    additional_info = Column(String(250), nullable=True)
