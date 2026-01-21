from module import engine, Student
from sqlalchemy.orm import sessionmaker
import click
import uuid

Session = sessionmaker(bind=engine)
session = Session()

@click.group
def cli():
    """A tool for groubing command line interface"""
    pass

@cli.command()
@click.option('--name','-n',nargs=2,help="Add First & Last student's name to the system",type= str)
def add (name):
    """Add a new student to the system"""
    s_name = (name[0] + " " + name[1]).title()
    s_id = uuid.uuid4()
    student = Student(name=s_name,id=s_id)
    session.add(student)
    session.commit()
    click.secho(f'{s_name} is added to the system successfully, its ID = {s_id}',fg='green')
    click.secho(f"Note: Don't share your ID, you use it to update & delete",fg='red')

@cli.command()
def update():
    pass

@cli.command()
@click.confirmation_option(prompt="Are you sure? you'll delete the student from the sys..")
@click.option("--identify",'-i',help="Delete the student from the system by its ID",type=click.UUID)
def delete(identify):
    """Delete a student from the system by its ID"""
    del_student = session.query(Student).filter_by(id=identify).one_or_none()
    if del_student:
        session.delete(del_student)
        session.commit()
        click.secho(f'Student: {del_student.name} with id : {del_student.id} is deleted successfully',fg='green')
    else:
        click.secho("Student not found!",fg='red')
        
        
@cli.command()
def view():
    """View all students in the system"""
    students = session.query(Student).all()
    if not students:
        click.secho("No students found!", fg="red")
    else:
        for s in students:
            click.secho(f"ID: {s.id} | Name: {s.name}", fg="blue")


@cli.command()
def info(): #use this command to guide the user 
    """Display information about the system"""
    click.secho("University Course Enrollment System",blink=True,fg='blue',bold=True)
    click.secho('Welcome to our System!',fg='green')


#learn the best way to add courses than edit the engine base and complete the ather functions
