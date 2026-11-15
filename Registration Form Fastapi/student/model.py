from sqlalchemy import Column,String,Integer
from database.db import Base

class Student(Base):
    __tablename__ = "registration_form_data"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    fathername = Column(String)
    cnic = Column(String)
    email = Column(String)
    phone = Column(String)
    gender = Column(String)
    address = Column(String)
    city = Column(String)
    country = Column(String)
    

