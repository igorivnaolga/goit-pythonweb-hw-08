from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import date


class ContactBase(BaseModel):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: EmailStr
    phone: str
    birthday: date
    info: Optional[str]


class ContactResponse(ContactBase):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    info: str

    model_config = ConfigDict(from_attributes=True)
