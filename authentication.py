from jose import jwt , JWTError
from datetime import datetime , timedelta
import schemas , models
from fastapi import Depends , status , HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import session 
from database import engine , get_db 



token_scheme = OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY = "JSKAJKKJ22534256as5a7sas5as5a"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data : dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode , SECRET_KEY , algorithm=ALGORITHM)

    return encoded_jwt

def verify_acces_token(token:str , credentials_exception):
    try :
        payload = jwt.decode( token , SECRET_KEY , algorithms= ALGORITHM)
        user_id :str = payload.get("user_id")
        if user_id is None:
            raise credentials_exception
        return schemas.TokenData(id=str(user_id))
    except JWTError:
        raise credentials_exception
    

def get_current_user(token : str = Depends(token_scheme) ,db : session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code= status.HTTP_401_UNAUTHORIZED ,
        detail=" could not validate",
        headers={"WWW-Authenticate": "Bearer"}
    )
    token_data = verify_acces_token(token ,credentials_exception )
    user = db.query(models.user).filter(models.User.id == token_data.id).first()
    if user is None :
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED ,
            detail="user not autherized"
        )
    return user


