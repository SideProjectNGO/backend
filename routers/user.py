from fastapi import APIRouter , Depends , status, HTTPException
import models , schemas
from database import get_db , engine
from sqlalchemy.orm import session
from typing import List


router = APIRouter(tags=['users'])
models.Base.metadata.create_all(bind=engine)





@router.post("/user" , status_code= status.HTTP_201_CREATED , response_model= schemas.RespondUser)
async def create_user(new_user = schemas.CreateUser , db : session= Depends(get_db)):
    new_user = models.User(**new_user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/user" , status_code= status.HTTP_200_OK , response_model= schemas.RespondUser)
async def get_users(db : session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/user/{id}" , status_code= status.HTTP_302_FOUND , response_model= schemas.RespondUser)
async def search_user(id: int , db :session = Depends(get_db)):
    user= db.query(models.User).filter(models.User.id  == id).first()
    if user is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail="user not found"
        )
    return user

@router.put("/user/{id}" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.RespondUser)
async def update_role(id : int , new_role: schemas.UpdateUser , db:session =Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail="user not found"
        )
    for key , value in new_role.dict().items():
        setattr(user , key , value)

    db.commit()
    db.refresh(user)
    return user 

@router.delete("/user/{id}" , status_code= status.HTTP_202_ACCEPTED)
async def delete_user(id : int  , db:session= Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail="user not found"
        )
    db.delete(user)
    db.commit()
    return "user has been deleted succesfully"



