from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True) 
    password = Column(String(255), nullable=False)  
    role = Column(String(200), nullable=False)

    forms = relationship("Form", back_populates="user", cascade="all, delete") 
    activities = relationship("Activity", back_populates="user", cascade="all, delete") 
    activities = relationship("Story", back_populates="user", cascade="all, delete")


class Form(Base):
    __tablename__ = "forms"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    phone = Column(String(20), nullable=True)
    message = Column(String(1000), nullable=True)
    cv_url = Column(String(255), nullable=True) 
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="forms")  


class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)  
    title = Column(String(250), nullable=False)
    content = Column(String(20000), nullable=False)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now()) 

    user = relationship("User", back_populates="activities")  


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)  
    title = Column(String(250), nullable=False)
    content = Column(String(20000), nullable=False)
    created_at = Column(DateTime, default=func.now())  
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now()) 

    user = relationship("User", back_populates="stories")  