from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class StudentModel(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    fatherName= Column(String)
    std_age= Column(Integer)