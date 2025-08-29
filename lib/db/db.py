from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, Instructor, Student, Course, Enrollment, Grade

class DatabaseManager:

    def __init__(self, db_url='sqlite:///school.db'):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    
    def get_all_instructors(self):
        with self.Session() as session:
            return session.query(Instructor).all()

    def find_instructor_by_id(self, id_):
        with self.Session() as session:
            return session.query(Instructor).get(id_)

    def create_instructor(self, name, subject):
        with self.Session() as session:
            new_instructor = Instructor(instructor_name=name, subject=subject)
            session.add(new_instructor)
            session.commit()
            return new_instructor

    def update_instructor(self, id_, name, subject):
        with self.Session() as session:
            instructor = session.query(Instructor).get(id_)
            if instructor:
                instructor.instructor_name = name if name else instructor.instructor_name
                instructor.subject = subject if subject else instructor.subject
                session.commit()
            return instructor

    def delete_instructor(self, id_):
        with self.Session() as session:
            instructor = session.query(Instructor).get(id_)
            if instructor:
                session.delete(instructor)
                session.commit()
                return True
            return False

    
    def get_all_students(self):
        with self.Session() as session:
            return session.query(Student).all()

    def find_student_by_id(self, id_):
        with self.Session() as session:
            return session.query(Student).get(id_)

    def create_student(self, name, email):
        with self.Session() as session:
            new_student = Student(student_name=name, student_email=email)
            session.add(new_student)
            session.commit()
            return new_student

    def update_student(self, id_, name, email):
        with self.Session() as session:
            student = session.query(Student).get(id_)
            if student:
                student.student_name = name if name else student.student_name
                student.student_email = email if email else student.student_email
                session.commit()
            return student

    def delete_student(self, id_):
        with self.Session() as session:
            student = session.query(Student).get(id_)
            if student:
                session.delete(student)
                session.commit()
                return True
            return False

    
    def get_all_courses(self):
        with self.Session() as session:
            return session.query(Course).all()

    def find_course_by_name(self, name):
        with self.Session() as session:
            return session.query(Course).filter_by(course_name=name).first()

    def find_course_by_id(self, id_):
        with self.Session() as session:
            return session.query(Course).get(id_)

    def create_course(self, name, instructor_id):
        with self.Session() as session:
            instructor = session.query(Instructor).get(instructor_id)
            if not instructor:
                return None
            new_course = Course(course_name=name, instructor_id=instructor_id)
            session.add(new_course)
            session.commit()
            return new_course

    def update_course(self, id_, name, instructor_id):
        with self.Session() as session:
            course = session.query(Course).get(id_)
            if course:
                if name:
                    course.course_name = name
                if instructor_id:
                    course.instructor_id = instructor_id
                session.commit()
            return course

    def delete_course(self, id_):
        with self.Session() as session:
            course = session.query(Course).get(id_)
            if course:
                session.delete(course)
                session.commit()
                return True
            return False

    