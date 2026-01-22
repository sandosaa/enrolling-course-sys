from modules import Student, Course
from db import session
from init import course_map
import click
import uuid

@click.group
def cli():
    """A tool for groubing command line interface"""
    pass

@cli.command()
@click.option('--name','-n',nargs=2,help="Add First & Last student's name to the system",type= str)
def create (name):
    """Add a new student to the system"""
    s_name = (name[0] + " " + name[1]).title()
    s_id = uuid.uuid4()
    student = Student(name=s_name,id=s_id)
    session.add(student)
    session.commit()
    session.close()
    click.secho(f'{s_name} is added to the system successfully, its ID = {s_id}',fg='green')
    click.secho(f"Note: Don't share your ID, you use it to update & delete",fg='red')

@cli.command()
@click.option("--identify", '-i', help="ID used for editing the courses", type=click.UUID)
@click.option("--append", "-a", help="++ course")
@click.option("--delete", "-d", help="-- course")
def update(identify, append, delete):
    """Update a student's enrolled courses by its ID"""
    if not identify:
        click.secho("You should enter the ID!", fg='red')
        return

    student = session.query(Student).filter_by(id=identify).one_or_none()
    if not student:
        click.secho(f"The student with ID: {identify} is not found", fg='red')
        return

    if append:
        append = append.upper()
        subject = course_map.get(append)
        if subject:
            sub = session.query(Course).filter_by(subject=subject).first()
            if sub not in student.courses:
                student.courses.append(sub)
                session.commit()
                click.secho(f"Course \"{subject}\" added successfully.", fg='green')
            else:
                click.secho(f"You enrolled \"{subject}\" before!", fg='red')
        else:
            click.secho("Invalid course code!", fg='red')

    if delete:
        delete = delete.upper()
        subject = course_map.get(delete)
        if subject:
            sub = session.query(Course).filter_by(subject=subject).first()
            if sub in student.courses:
                student.courses.remove(sub)
                session.commit()
                click.secho(f"Course \"{subject}\" removed successfully.", fg='green')
            else:
                click.secho(f"You are not enrolled in \"{subject}\".", fg='red')
        else:
            click.secho("Invalid course code!", fg='red')

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
            click.secho(f"ID: {s.id} | Name: {s.name} & Enrolled {[sub.subject for sub in s.courses]}", fg="blue")


@cli.command()
def list_courses():
    """List all available courses with codes and IDs"""
    click.secho("Available Courses:", fg="green", bold=True)
    printed = set()
    for key, subject in course_map.items():
        if subject not in printed:
            codes = [k for k, v in course_map.items() if v == subject]
            click.secho(f"{subject} -> options: {', '.join(codes)}", fg="blue")
            printed.add(subject)
            

@cli.command()
@click.option('--id', prompt="Student ID", type=click.UUID)
def student_info(id):
    """Display information about a specific student"""
    student = session.query(Student).filter_by(id=id).one_or_none()
    if student:
        click.secho(f"Name: {student.name}", fg="green", bold=True)
        if student.courses:
            click.secho("Enrolled Courses:", fg="green")
            for c in student.courses:
                click.secho(f"- {c.subject}", fg="blue")
        else:
            click.secho("No courses enrolled yet.", fg="red")
    else:
        click.secho("Student not found!", fg="red")
        

@cli.command()
def info(): #use this command to guide the user 
    """Display information about the system"""
    click.secho("University Course Enrollment System",blink=True,fg='blue',bold=True)
    click.secho('Welcome to our System!',fg='green')


#learn the best way to add courses than edit the engine base and complete the ather function