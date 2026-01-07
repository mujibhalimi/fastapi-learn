from fastapi import FastAPI
from schema import Student
from database import session, engine
from models import Base,StudentModel as StdModel
app = FastAPI()

@app.get('/')
def greeting():
    return "Hello World"

students = [
    Student(id=1,name="ahmad",fatherName="Ali",std_age=30),
    Student(id=2,name="Raheem",fatherName="Kareem",std_age=20),
]

def init_db():
    # connection open
    # query
    # connection close
    Base.metadata.create_all(bind=engine)
    db=session()
    count = db.query(StdModel).count()
    if count == 0:
        for student in students:
            db.add(StdModel(**student.model_dump()))
            db.commit()

    db.close()

init_db()

@app.get('/students')
def all_students():
    db= session()
    db_students= db.query(StdModel).all()

    return db_students


@app.post('/student')
def create(student: Student):
    db= session()
    db_student = StdModel(**student.model_dump())
    db.add(db_student)
    db.commit()
    return "Student Added Successfully"

@app.get('/student/{id}')
def get_student(id:int):
    db= session()
    db_student = db.query(StdModel).filter(StdModel.id == id).first()
    if db_student:
        return db_student
    else:
        return "Not found"

@app.delete('/student/{id}')
def delete_std(id:int):
    db= session()
    db_student = db.query(StdModel).filter(StdModel.id== id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
        return "Student Deleted successfully"
    else:
        return "Not Found"
    

@app.put('/student/{id}')
def update_std(id:int, student: Student):
    db = session()
    db_student = db.query(StdModel).filter(StdModel.id== id).first()
    if db_student:
        db_student.name = student.name
        db_student.fatherName= student.fatherName
        db_student.std_age= student.std_age
        db.commit()
        return " Student Updated successfully"
    else:
        return "Not Found"
    
