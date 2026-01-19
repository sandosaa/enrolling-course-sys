from sqlalchemy import create_engine, Column,String,types
from sqlalchemy.orm import declarative_base

data_base_url = "sqlite:///database.db"
engine = create_engine(data_base_url)
Base = declarative_base()

class Student(Base):
    __tablename__="Students"

    id=Column(types.UUID,primary_key=True)
    name=Column(String)
    
    #course=Column()


Base.metadata.create_all(engine)