from pydantic import BaseModel

class Register(BaseModel):
    email: str
    password: str

class Login(BaseModel):
    email: str
    password: str

class UserOut(BaseModel):
    id: int
    email: str

class ItemCreate(BaseModel):
    title: str

class ItemOut(BaseModel):
    id: int
    title: str
    user_id: int
