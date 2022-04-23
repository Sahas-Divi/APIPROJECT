from datetime import datetime
from operator import le
from typing import Optional, Literal
from pydantic import BaseModel, EmailStr
from pydantic.types import conint


class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True

class PostCreate(PostBase):
    pass


class UsersOut(BaseModel): 
    email:EmailStr
    id : int
    created_at: datetime
    
    class Config():
        orm_mode = True

class Post(PostBase):
    created_at: datetime
    id : int
    owner_id : int
    owner : UsersOut
    
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes:int

    class Config:
        orm_mode = True




class UsersCreate(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str]=None


class Vote(BaseModel):
    post_id : int
    dir: conint(le=1)