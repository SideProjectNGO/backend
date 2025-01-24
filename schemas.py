from pydantic import BaseModel , EmailStr , ConfigDict
from typing import Optional 
import datetime



#################### User ##################### 

class RespondUser(BaseModel):
    id: int
    name: str 
    email: EmailStr
    role: str 
    class config:
        orm_mode = True 

class CreateUser(BaseModel):
    name : str 
    email : EmailStr
    password: str 
    role : str 

class UpdateUser(BaseModel):
    role: str
    


##################token######################

class Token(BaseModel):
    access_token : str
    token_type : str

class TokenData(BaseModel):
    id : Optional[str]= None


############## Form ###########################

class CreateForm(BaseModel):
    phone: str 
    message: str
    cv_url: str 
    status:str 

class RespondForm(BaseModel):
    id: int
    user_id: int 
    email : EmailStr
    phone: str 
    message: str
    cv_url: str 
    status:str 
    created_at: datetime 
    model_config = ConfigDict(arbitrary_types_allowed=True)

    class config:
        orm_mode = True 


######################### activities ##############################

class CreateActivity(BaseModel):
    title : str 
    content: str 

class RespondActivity(BaseModel):
    id : int 
    author_id: int 
    title : str 
    content: str 
    created_at : datetime
    updated_at: datetime
    model_config = ConfigDict(arbitrary_types_allowed=True)
    class config : 
        orm_mode = True

class UpdateActivity(BaseModel):
    title : str 
    content: str 


################################# stories ############################# 

class CreateStory(BaseModel):
    title : str 
    content: str 

class RespondStory(BaseModel):
    id : int 
    author_id: int 
    title : str 
    content: str 
    created_at : datetime
    updated_at: datetime
    model_config = ConfigDict(arbitrary_types_allowed=True)
    class config : 
        orm_mode = True

class UpdateStory(BaseModel):
    title : str 
    content: str 