from pydantic import BaseModel, EmailStr


class Auth(BaseModel):
    email: EmailStr
    password: str
