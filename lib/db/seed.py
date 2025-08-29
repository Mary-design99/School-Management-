from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Instructor, Student, Course, Enrollment, Grade

if __name__ == '__main__':
    engine = create_engine('sqlite:///school.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    # This line creates all the tables defined in your models.py
    Base.metadata.create_all(engine)

    # You were missing commas and had incorrect variables.
    instructor1 = Instructor(instructor_name="Alice", subject="Literature")
    instructor2 = Instructor(instructor_name="Maurice", subject="Kiswahili")
    instructor3 = Instructor(instructor_name="Laureen", subject="Physics")
    instructor4 = Instructor(instructor_name="Mercy", subject="History")
    instructor5 = Instructor(instructor_name="Robert", subject="Biology")
    instructor6 = Instructor(instructor_name="Marvin", subject="Computer")

    session.add_all([
        instructor1, instructor2, instructor3,
        instructor4, instructor5, instructor6
    ])
    session.commit()

    student1 = Student(student_name="Beatrive",student_email="betrice@email.com")
    student2 = Student(student_name="Mary",student_email="mary@email.com")
    student3 = Student(student_name="John", student_email="john@email.com")
    student4 = Student(student_name="Jane", student_email="jane@email.com")
    student5 = Student(student_name="Peter", student_email="peter@email.com")
    session.add_all([student1, student2,student4,student3,student5])
    session.commit()

    course1 = Course(course_name="Introduction to Literature", instructor=instructor1)
    course2 = Course(course_name="Advanced Physics", instructor=instructor3)
    course3 = Course(course_name="Introduction to History", instructor=instructor4)
    course4 = Course(course_name="Advanced Biology", instructor=instructor5)
    course5 = Course(course_name="Computer Science 101", instructor=instructor6)
    session.add_all([course1, course2, course3, course4, course5])
    session.commit()

    enrollment1 = Enrollment(student=student1, course=course1)
    enrollment2 = Enrollment(student=student2, course=course2)

    
    session.add_all([enrollment1, enrollment2])
    session.commit()

    grade1 = Grade(grade=95, enrollment=enrollment1)
    grade2 = Grade(grade=88, enrollment=enrollment2)
    session.add_all([grade1, grade2])
    session.commit()
    
    session.close()

    print("Database seeded successfully!")
