from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Instructor(Base):
    __tablename__ = 'instructors'
    id = Column(Integer, primary_key=True)
    instructor_name = Column(String) 
    subject = Column(String)
    courses = relationship('Course', back_populates='instructor')
    
    def __repr__(self):
        return f"Instructor(id={self.id}, name={self.instructor_name}, subject={self.subject})"

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    student_name = Column(String)
    student_email = Column(String)
    enrollments = relationship('Enrollment', back_populates='student')

    def __repr__(self):
        return f"Student(id={self.id}, name={self.student_name}, email={self.student_email})"

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_name = Column(String)
    instructor_id = Column(Integer, ForeignKey('instructors.id')) 
    instructor = relationship('Instructor', back_populates='courses') 
    enrollments = relationship('Enrollment', back_populates='course')

    def __repr__(self):
        return f"Course(id={self.id}, name={self.course_name})"

class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    student = relationship('Student', back_populates='enrollments')
    course = relationship('Course', back_populates='enrollments')  # <-- fixed here
    grade = relationship('Grade', uselist=False, back_populates='enrollment')

    def __repr__(self):
        return f"Enrollment(id={self.id}, student_id={self.student_id}, course_id={self.course_id})"

class Grade(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    enrollment_id = Column(Integer, ForeignKey('enrollments.id'))
    enrollment = relationship('Enrollment', back_populates='grade')
    
    def __repr__(self):
        return f"Grade(id={self.id}, value={self.grade})"