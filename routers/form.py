from fastapi import status , APIRouter , HTTPException , Depends
import models , schemas , authentication
from database import get_db , engine
from sqlalchemy.orm import session




router = APIRouter(tags=["form"])
models.Base.metadata.create_all(bind=engine)



@router.post("/form" , status_code= status.HTTP_201_CREATED , response_model=schemas.RespondForm)
async def create_post(new_form : schemas.CreateForm , db: session = Depends(get_db) , current_user :int = Depends(authentication.get_current_user)):
    new_form = models.Form(user_id=current_user.id,**new_form.dict())
    db.add(new_form)
    db.commit()
    db.refresh(new_form)
    return new_form 


@router.get("/form" , status_code=status.HTTP_202_ACCEPTED , response_model= schemas.RespondForm)
async def get_all_forms(db : session = Depends(get_db)):
    forms = db.query(models.Form).all()
    return forms


@router.get("/form/{id}" , status_code=status.HTTP_302_FOUND , response_model=schemas.RespondForm)
async def get_one_form(id : int  , db:session=Depends(get_db)):
    form = db.query(models.Form).filter(models.Form.id == id).first()
    if form is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , 
            detail="id is not found"
        )
    return form

@router.delete("form/{id}" , status_code=status.HTTP_410_GONE )
async def delete_form(id: int , db: session=Depends(get_db)):
    form = db.query(models.Form).filter(models.Form.id == id).first()
    if form is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND , 
            detail="id is not found"
        )
    db.delete(form)
    db.commit()
    return "form has been deleted succesfully"