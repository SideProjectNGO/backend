from fastapi import  APIRouter , HTTPException , status , Depends
import database , models , schemas , authentication , hashed_password
from sqlalchemy.orm import session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm


router = APIRouter(tags=["login"])



@router.post("/login" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.Token)
async def login(user_data : OAuth2PasswordRequestForm = Depends() , db: session =Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_data.username).first()
    if user  is None:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="invalid data"
        )
    if not hashed_password.verify(user_data.password , user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="invalid data"
        )
    access_token = authentication.create_access_token(data={"user_id":user.id})

    return {"access_token": access_token, "token_type": "bearer"}