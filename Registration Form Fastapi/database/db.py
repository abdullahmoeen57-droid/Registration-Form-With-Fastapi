from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
database_url = "postgresql://postgres:abdullah1@localhost:5432/student_db" 
engine = create_engine(database_url)
Sessionlocal = sessionmaker(bind=engine)
Base = declarative_base()
def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()