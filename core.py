from module import Student,Course,session 
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
                if ('1' in append) or append=='DB':
                    sub= session.query(Course).get(1)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Databases\" before!",fg='red')

                if ('2' in append) or append=='CI':
                    sub= session.query(Course).get(2)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Computational Intelligence\" before!",fg='red')

                if ('3' in append) or append=='DS':
                    sub= session.query(Course).get(3)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Data Structures\" before!",fg='red')

                if ('4' in append) or append=='NLP':
                    sub= session.query(Course).get(4)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Natural Language Processing\" before!",fg='red')

                if ('5' in append) or append=='OS':
                    sub= session.query(Course).get(5)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Operating Systems\" before!",fg='red')

                if ('6' in append) or append=='MASD':
                    sub= session.query(Course).get(6)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Multi Agent Systems Design\" before!",fg='red')

                if ('7' in append) or append=='CS':
                    sub= session.query(Course).get(7)
                    if sub not in s_t.courses:
                        s_t.courses.append(sub)
                        session.commit()
                    else:
                        click.secho(f"You enrolled \"Computer Security\" before!",fg='red')
                
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
            click.secho(f"ID: {s.id} | Name: {s.name} & Enrolled {[sub.subject for sub in s.courses]}", fg="blue")

@cli.command()
def info(): #use this command to guide the user 
    """Display information about the system"""
    click.secho("University Course Enrollment System",blink=True,fg='blue',bold=True)
    click.secho('Welcome to our System!',fg='green')


#learn the best way to add courses than edit the engine base and complete the ather function