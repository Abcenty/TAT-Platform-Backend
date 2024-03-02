from pydantic import BaseModel, EmailStr


class Auth(BaseModel):
    email: EmailStr
    password: str
    
    
class Registration(BaseModel):
    last_name: str
    first_name: str
    patronymic: str
    email: EmailStr
    password: str
