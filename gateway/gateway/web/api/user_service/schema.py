from pydantic import BaseModel


class Auth(BaseModel):
    email: str
    password: str
