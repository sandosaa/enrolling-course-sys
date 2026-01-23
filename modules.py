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

course_map = {
    '1': 'Databases', 'DB': 'Databases',
    '2': 'Computational Intelligence', 'CI': 'Computational Intelligence',
    '3': 'Data Structures', 'DS': 'Data Structures',
    '4': 'Natural Language Processing', 'NLP': 'Natural Language Processing',
    '5': 'Operating Systems', 'OS': 'Operating Systems',
    '6': 'Multi Agent Systems Design', 'MASD': 'Multi Agent Systems Design',
    '7': 'Computer Security', 'CS': 'Computer Security'
}

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
    is_exist=session.query(Course).filter_by(subject=i).first()
    if not is_exist:
        session.add(Course(subject=i))
        session.commit()
