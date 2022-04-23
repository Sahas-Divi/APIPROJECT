from fastapi import FastAPI, Response,status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List

router = APIRouter(prefix = "/users", tags = ["Users"])

@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.UsersOut)
def create_user(user: schemas.UsersCreate ,db: Session = Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

@router.get("/{id}",response_model=schemas.UsersOut)
def get_user(id:int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail = "User with id {} does not exist".format(id))
    return user

@router.get("/", response_model=List[schemas.UsersOut])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.delete("/{id}",status_code = status.HTTP_204_NO_CONTENT)
def delete_user(id:int,db: Session = Depends(get_db)):
    deleted_user = db.query(models.User).filter(models.User.id==id)
    if deleted_user.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail = "User with id {} does not exist".format(id))
    deleted_user.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
 