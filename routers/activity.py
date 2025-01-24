from fastapi import status , APIRouter , HTTPException , Depends
from sqlalchemy.orm import session
from database import engine , get_db
import models , schemas



router = APIRouter(tags=["activities"])
models.Base.metadata.create_all(bind= engine)





@router.post("/activity" , status_code= status.HTTP_201_CREATED , response_model= schemas.RespondActivity)
async def create_post(activity : schemas.CreateActivity , db : session = Depends(get_db)):
    activity = models.Activity(**activity.dict())
    db.add(activity)
    db.commit()
    db.refresh(activity)
    return activity

@router.get("/activity" , status_code= status.HTTP_200_OK , response_model=schemas.RespondActivity)
async def get_all_activities(db: session =Depends(get_db)):
    activities  = db.query(models.Activity).all()
    return activities


@router.get("/activity/{id}" , status_code=status.HTTP_302_FOUND , response_model= schemas.RespondActivity)
async def get_one_activity( id : int  , db : session = Depends(get_db)):
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
    if activity is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " article id not found"
        )
    return activity

@router.delete("/activity/{id}" , status_code= status.HTTP_202_ACCEPTED )
async def delete_user( id : int  , db : session = Depends(get_db)):
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
    if activity is None : 
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " article id not found"
        )
    db.delete(activity)
    db.commit()
    return "activity has been deleted "


@router.put("/activity/{id}" , status_code= status.HTTP_202_ACCEPTED , response_model= schemas.RespondActivity)
async def update_activity(update_activity : schemas.UpdateActivity , id : int , db : session = Depends(get_db)):
    activity = db.query(models.Activity).filter(models.Activity.id == id).first()
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
    
