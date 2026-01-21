from module import engine, Student,sessionmaker,Course
import click
import uuid
Session =sessionmaker(bind= engine)
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
@click.option("--identify",'-i',help="ID used for editing the courses",type=click.UUID)
@click.option("--append","-a",help="++ course")
@click.option("--delete","-d",help="-- course")
def update(identify,append,delete):
    if not identify:
        click.secho("You should enter the ID!",fg='red')
    else:
        s_t= session.query(Student).filter_by(id=identify).one_or_none()
        if s_t:
            if append:
                append=append.upper()
                if ('1' in add) or add=='DB':
                    s_t.courses.append(Course(id=1))
                    session.add(s_t)
                    session.commit()
                if ('2' in add) or add=='CI':
                    s_t.courses.append(Course(id=2))
                    session.add(s_t)
                    session.commit()
                if ('3' in add) or add=='DS':
                    s_t.courses.append(Course(id=3))
                    session.add(s_t)
                    session.commit()
                if ('4' in add) or add=='NLP':
                    s_t.courses.append(Course(id=4))
                    session.add(s_t)
                    session.commit()
                if ('5' in add) or add=='OS':
                    s_t.courses.append(Course(id=5))
                    session.add(s_t)
                    session.commit()
                if ('6' in add) or add=='MASD':
                    s_t.courses.append(Course(id=6))
                    session.add(s_t)
                    session.commit()
                if ('7' in add) or add=='CS':
                    s_t.courses.append(Course(id=7))
                    session.add(s_t)
                    session.commit()   
            if delete:
                pass
        else:
            click.secho(f"The student with ID: {identify} is not found",fg='red')


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


#learn the best way to add courses than edit the engine base and complete the ather function