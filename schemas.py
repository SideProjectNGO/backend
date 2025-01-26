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


######################### articles ##############################

class CreateArticle(BaseModel):
    title : str 
    content: str 
    summary: str
    main_photo_url: str
    sub_photo_urls: str
    social_share_links: str

class RespondArticle(BaseModel):
    id : int 
    author_id: int 
    title : str 
    content: str 
    summary: str
    main_photo_url: str
    sub_photo_urls: str
    social_share_links: str
    created_at : datetime
    updated_at: datetime
    model_config = ConfigDict(arbitrary_types_allowed=True)
    class config : 
        orm_mode = True

class UpdateArticle(BaseModel):
    title : str 
    content: str 
    summary: str
    main_photo_url: str
    sub_photo_urls: str
    social_share_links: str


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





############################## activities ###############################
class CreateActivity(BaseModel):
    title : str 
    description: str 
    date : str


class RespondActivity(BaseModel):
    id : int 
    author_id: int 
    title : str 
    description: str 
    created_at : datetime
    model_config = ConfigDict(arbitrary_types_allowed=True)
    class config : 
        orm_mode = True

