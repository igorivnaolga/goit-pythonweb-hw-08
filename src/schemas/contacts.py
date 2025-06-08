from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date


class ContactBase(BaseModel):
    first_name: str = Field(..., max_length=50)
    last_name: str = Field(..., max_length=50)
    email: EmailStr
    phone_number: str = Field(..., max_length=20)
    birthday: date
    additional_info: Optional[str] = Field(None, max_length=250)


class ContactCreate(ContactBase):
    pass  # Наслідує всі поля від ContactBase


class ContactUpdate(BaseModel):
    first_name: Optional[str] = Field(None, max_length=50)
    last_name: Optional[str] = Field(None, max_length=50)
    email: Optional[EmailStr]
    phone_number: Optional[str] = Field(None, max_length=20)
    birthday: Optional[date]
    additional_info: Optional[str] = Field(None, max_length=250)


class ContactResponse(ContactBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
