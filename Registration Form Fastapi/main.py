from fastapi import FastAPI, Depends,Form
from sqlalchemy.orm import Session
from database.db import engine, get_db, Base
from student.model import Student
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


# Database table create
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return FileResponse("templates/students.html")
@app.post("/register")
def student_data(
    name: str = Form(...),
    fathername: str = Form(...),
    cnic: str = Form(...),
    email: str = Form(...),
    phone: str = Form(...),
    gender: str = Form(...),
    address: str = Form(...),
    city: str = Form(...),
    country: str = Form(...),
    db: Session = Depends(get_db)
    ):
    new_student = Student(
        name=name,
        fathername=fathername,
        cnic=cnic,
        email=email,
        phone=phone,
        gender=gender,
        address=address,
        city=city,
        country=country 
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return {"message" : "Student Registration SuccessFully !",
            "Student" : new_student   
            }