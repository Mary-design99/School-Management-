import sys
from db.models import Instructor, Student, Course, Enrollment, Grade

def exit_program():
    print("Goodbye!")
    sys.exit()

def list_instructors(db):
    instructors = db.get_all_instructors()
    if instructors:
        for instructor in instructors:
            print(instructor)
    else:
        print("No instructors found.")

def find_instructor_by_id(db):
    try:
        id_ = int(input("Enter the instructor's id: "))
        instructor = db.find_instructor_by_id(id_)
        print(instructor) if instructor else print(f"Instructor {id_} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")

def create_instructor(db):
    name = input("Enter the instructor's name: ")
    subject = input("Enter the instructor's subject: ")
    instructor = db.create_instructor(name, subject)
    if instructor:
        print(f'Success: {instructor}')
    else:
        print("Error creating instructor.")

def delete_instructor(db):
    try:
        id_ = int(input("Enter the instructor's id: "))
        if db.delete_instructor(id_):
            print(f'Instructor {id_} deleted')
        else:
            print(f'Instructor {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a number.")

def list_students(db):
    students = db.get_all_students()
    if students:
        for student in students:
            print(student)
    else:
        print("No students found.")

def create_student(db):
    name = input("Enter the student's name: ")
    email = input("Enter the student's email: ")
    student = db.create_student(name, email)
    if student:
        print(f'Success: {student}')
    else:
        print("Error creating student.")

def delete_student(db):
    try:
        id_ = int(input("Enter the student's id: "))
        if db.delete_student(id_):
            print(f'Student {id_} deleted')
        else:
            print(f'Student {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a number.")

def list_courses(db):
    courses = db.get_all_courses()
    if courses:
        for course in courses:
            print(course)
    else:
        print("No courses found.")

def find_course_by_name(db):
    course_name = input("Enter the course's name: ")
    course = db.find_course_by_name(course_name)
    print(course) if course else print(f'Course {course_name} not found')

def find_course_by_id(db):
    try:
        id_ = int(input("Enter the course's id: "))
        course = db.find_course_by_id(id_)
        print(course) if course else print(f"Course {id_} not found")
    except ValueError:
        print("Invalid input. Please enter a number.")

def update_course(db):
    try:
        id_ = int(input("Enter the course's id: "))
        course = db.find_course_by_id(id_)
        if course:
            print(f"Current name: {course.course_name}")
            name = input("Enter the course's new name: ")
            print(f"Current instructor ID: {course.instructor_id}")
            try:
                instructor_id = int(input("Enter the new instructor ID: "))
            except ValueError:
                print("Invalid instructor ID. Please enter a number.")
                return
            updated_course = db.update_course(id_, name, instructor_id)
            if updated_course:
                print(f'Success: {updated_course}')
            else:
                print(f'Course {id_} not found or instructor ID {instructor_id} is invalid.')
        else:
            print(f'Course {id_} not found')
    except ValueError:
        print("Invalid input. Please enter a number.")