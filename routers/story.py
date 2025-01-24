from fastapi import APIRouter , Depends , status , HTTPException
from sqlalchemy.orm import session
import models , database , schemas
from database import get_db , engine



router = APIRouter(tags=["stories"])
models.Base.metadata.create_all(bind = engine)



@router.post("/story" ,  status_code= status.HTTP_201_CREATED , response_model= schemas.RespondStory)
async def create_story(story : schemas.CreateStory , db: session =Depends(get_db)):
    story = models.Story(**story.dict())
    db.add(story)
    db.commit()
    db.refresh(story)
    return story

@router.get("/story" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.RespondStory)
async def get_all_stories(db: session =Depends(get_db)):
    stories = db.query(models.Story).all()
    return stories

@router.get("/story/{id}" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.RespondStory )
async def get_one_story(id:int , db :session =Depends(get_db)):
    story = db.query(models.Story).filter(models.Story.id == id).first()
    if story is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail="story not found"
        )
    return story

@router.put("/story/{id}" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.RespondStory)
async def update_story(id :int, updateStory:schemas.UpdateStory , db: session=Depends(get_db)):
    story = db.query(models.Story).filter(models.Story.id == id).first()
    if story is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail="story not found"
        )
    for key , value in updateStory.dict().items():
        setattr(story ,key , value)

    db.commit()
    db.refresh(story)
    return story


@router.delete("/story/{id}"  , status_code= status.HTTP_202_ACCEPTED)
async def delete_story(id: int , db:session =Depends(get_db)):
    story = db.query(models.Story).filter(models.Story.id == id).first()
    if story is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail="story not found"
        )
    db.delete(story)
    db.commit()
    return "story has been deleted succesfully"