from pydantic import BaseModel
class StudentCreate(BaseModel):
    name : str
    fathername : str
    cnic : str
    email : str
    phone : str
    gender : str
    address : str
    city : str
    country : str
    