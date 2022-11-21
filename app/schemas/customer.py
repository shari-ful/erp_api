from pydantic import BaseModel
import datetime


class CustomerBase(BaseModel):
    customer_id: int


class CustomerQuickCreate(BaseModel):
    email: str
    phone: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "email@example.com",
                "phone": "+8801234567890"
            }
        }

class CustomerQuickUpdate(BaseModel):
    email: str
    phone: str

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "email@example.com",
                "phone": "+8801234567890"
            }
        }

class CustomerDelete(BaseModel):
    customer_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "customer_id": 11
        }

class Customer(CustomerQuickCreate):
    name: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    company: str | None = None
    comment: str | None = None
    currency: str | None = None
    default_billing_id: str | None = None
    default_shipping_id: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "john@gmail.com",
                "phone": "+8801234567890",
                "name": "John Bell",
                "first_name": "John",
                "last_name": "Bell",
                "company": "Intellier",
                "comment": "software development",
                "currency": "BDT",
                "default_billing_id": "bl123",
                "default_shipping_id": "bl456",
                "addresses": "ABC Tower, Jasimuddin Avenue"
            }
        }

class CustomerUpdate(CustomerQuickUpdate):
    name: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    company: str | None = None
    comment: str | None = None
    currency: str | None = None
    default_billing_id: str | None = None
    default_shipping_id: str | None = None

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "customer_id": 11,
                "email": "john@gmail.com",
                "phone": "+8801234567890",
                "name": "John Bell",
                "first_name": "John",
                "last_name": "Bell",
                "company": "Intellier",
                "comment": "software development",
                "currency": "BDT",
                "default_billing_id": "bl123",
                "default_shipping_id": "bl456"
            }
        }

class CustomerResponse(Customer, CustomerQuickCreate):
    customer_id: int

    class Config:
        schema_extra = {
            "example": {
                "customer_id": 11,
                "email": "john@gmail.com",
                "phone": "+8801234567890",
                "name": "John Bell",
                "first_name": "John",
                "last_name": "Bell",
                "company": "Intellier",
                "comment": "software development",
                "currency": "BDT",
                "default_billing_id": "bl123",
                "default_shipping_id": "bl456"               
            }
        }
class SuccessMessage(BaseModel):
    success: str
    class Config:
        schema_extra = {
            "example": {
                "success": "created"
            }
        }