from pydantic import BaseModel, UUID4, Field, EmailStr
from datetime import datetime


class UserInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    email: EmailStr = Field(min_length=1, max_length=120)
    password: str = Field(min_length=1, max_length=120)


class UserOutput(BaseModel):
    id: UUID4
    name: str
    email: str