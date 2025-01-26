from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(200), nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    forms = relationship("Form", back_populates="user", cascade="all, delete")
    articles = relationship("Article", back_populates="user", cascade="all, delete")
    stories = relationship("Story", back_populates="user", cascade="all, delete")
    logs = relationship("AdminLog", back_populates="admin", cascade="all, delete")


class Form(Base):
    __tablename__ = "forms"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    message = Column(Text, nullable=True)
    cv_url = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False, default="pending")
    dob = Column(String(50), nullable=True)
    address = Column(String(255), nullable=True)
    days = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=func.now())

    user = relationship("User", back_populates="forms")


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(250), nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text, nullable=True)
    main_photo_url = Column(String(255), nullable=True)
    sub_photo_urls = Column(Text, nullable=True)
    publication_date = Column(DateTime, default=func.now())
    social_share_links = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="articles")


class Story(Base):
    __tablename__ = "stories"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    title = Column(String(250), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    user = relationship("User", back_populates="stories")


class Activity(Base):
    __tablename__ = "activities"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(250), nullable=False)
    description = Column(Text, nullable=False)
    date = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=func.now())


class AdminLog(Base):
    __tablename__ = "admin_logs"
    
    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    action = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    admin = relationship("User", back_populates="logs")
