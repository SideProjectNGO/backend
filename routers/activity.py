from fastapi import HTTPException , status , Depends ,APIRouter
from sqlalchemy.orm import session 
import models , schemas
from database import engine , get_db



router = APIRouter(tags=["activites"])
models.Base.metadata.create_all(bind=engine)



@router.post("/activity" , status_code=status.HTTP_201_CREATED , response_model= schemas.RespondActivity)
async def create_activity(newAct: schemas.CreateActivity , db: session= Depends(get_db)):
    newAct = models.Activity(**newAct.dict())
    db.add(newAct)
    db.commit()
    db.refresh(newAct)
    return newAct



@router.get("/activity" , status_code=status.HTTP_202_ACCEPTED , response_model= schemas.RespondActivity)
async def get_all_activity(db:session = Depends(get_db)):
    act = db.query(models.Activity).all()
    return act 



@router.get("/activity/{id}" , status_code=status.HTTP_202_ACCEPTED , response_model= schemas.RespondActivity)
async def get_one_user(id: int , db: session =Depends(get_db)):
    act = db.query(models.Activity).filter(models.Activity.id == id).first()
    if act is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " activity not found"
        )
    return act 


@router.delete("/activity/{id}" , status_code= status.HTTP_202_ACCEPTED )
async def delete_act(id :int , db: session=Depends(get_db)):
    act = db.query(models.Activity).filter(models.Activity.id == id).first()
    if act is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND , 
            detail= " activity not found"
        )
    db.delete(act)
    db.commit()
    return "act has been deleted succesfully"