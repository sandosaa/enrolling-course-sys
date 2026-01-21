from sqlalchemy import create_engine, Integer,Column,String,types,ForeignKey    
from sqlalchemy.orm import declarative_base,relationship,sessionmaker

data_base_url = "sqlite:///database.db"
engine = create_engine(data_base_url)
Base = declarative_base()

class stu_cour(Base): #associative
    __tablename__ = "link"
    id = Column(Integer,primary_key=True)
    id_student=Column("id_student",ForeignKey('Students.id'))
    id_course=Column("id_course",Integer,ForeignKey("Courses.id"))

class Student(Base):
    __tablename__="Students"
    id=Column(types.UUID,primary_key=True)
    name=Column(String)
    courses = relationship("Course",secondary="link",back_populates='students')
    
class Course(Base):
    __tablename__ ="Courses"
    id=Column(Integer,primary_key=True)
    subject=Column(String)
    students=relationship("Student",secondary="link",back_populates='courses')


Base.metadata.create_all(engine)

subjects=['Databases',
    'Computational Intelligence',
    'Data Structures',
    'Natural Language Processing',
    'Operating Systems',
    'Multi Agent Systems Design',
    'Computer Security']

Session =sessionmaker(bind= engine)
session = Session()
for i in subjects:
    session.add(Course(subject=i))
    session.commit()

