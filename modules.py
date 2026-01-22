from sqlalchemy import Column, Integer, String, ForeignKey, types
from sqlalchemy.orm import relationship
from db import Base

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


