from fastapi import FastAPI
import models 
from database import Base , engine
import psycopg2
from psycopg2.extras import RealDictCursor
from routers import user , login , form , activity



models.Base.metadata.create_all(bind=engine)
app= FastAPI()


try:
    conn = psycopg2.connect(host='localhost' , database='sideProject' , user='postgres' , password='kaddakadda' , cursor_factory= RealDictCursor)
    cursor = conn.cursor()
    print("we are connected to the database")
except:
    print("failed to connect to the database")



app.include_router(user.router)
app.include_router(login.router)
app.include_router(form.router)
app.include_router(activity.router)