from pydantic import BaseModel


class Student(BaseModel):
    name:str
    fatherName:str
    std_age:int