from pydantic import BaseModel


class Student(BaseModel):
    id:int
    name:str
    fatherName:str
    std_age:int