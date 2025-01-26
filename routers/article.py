from fastapi import status , APIRouter , HTTPException , Depends
from sqlalchemy.orm import session
from database import engine , get_db
import models , schemas



router = APIRouter(tags=["articles"])
models.Base.metadata.create_all(bind= engine)





@router.post("/article" , status_code= status.HTTP_201_CREATED , response_model= schemas.RespondArticle)
async def create_post(activity : schemas.CreateArticle , db : session = Depends(get_db)):
    activity = models.Article(**activity.dict())
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@router.get("/article" , status_code= status.HTTP_200_OK , response_model=schemas.RespondArticle)
async def get_all_article(db: session =Depends(get_db)):
    activities  = db.query(models.Article).all()
    return activities


@router.get("/article/{id}" , status_code=status.HTTP_302_FOUND , response_model= schemas.RespondArticle)
async def get_one_article( id : int  , db : session = Depends(get_db)):
    activity = db.query(models.Article).filter(models.Article.id == id).first()
    if activity is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " article id not found"
        )
    return activity

@router.delete("/article/{id}" , status_code= status.HTTP_202_ACCEPTED )
async def delete_user( id : int  , db : session = Depends(get_db)):
    activity = db.query(models.Article).filter(models.Article.id == id).first()
    if activity is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " article id not found"
        )
    db.delete(activity)
    db.commit()
    return "article has been deleted "


@router.put("/article/{id}" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.RespondArticle)
async def update_article(update_activity : schemas.UpdateArticle , id : int , db : session = Depends(get_db)):
    activity = db.query(models.Article).filter(models.Article.id == id).first()
    if activity is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " article id not found"
        )
    for key , value , in update_activity.dict().items():
        setattr(activity , key , value )

    db.commit()
    db.refresh(activity)
    return activity
    
