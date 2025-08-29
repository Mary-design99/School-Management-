

from db.db import DatabaseManager
from helpers import (
    exit_program,
    list_instructors,
    find_instructor_by_id,
    create_instructor,
    list_students,
    create_student,
    delete_student,
    list_courses,
    find_course_by_name,
    update_course
)

db = DatabaseManager()

if __name__ == '__main__':
    while True:
        print("\n--- Main Menu ---")
        print("1. Instructors")
        print("2. Students")
        print("3. Courses")
        print("0. Exit")
        choice = input("> ")

        if choice == '1':
            while True:
                print("\n--- Instructor Menu ---")
                print("1. List all instructors")
                print("2. Find instructor by ID")
                print("3. Create new instructor")
                print("0. Back to main menu")
                sub_choice = input("> ")
                if sub_choice == '1':
                    list_instructors(db)
                elif sub_choice == '2':
                    find_instructor_by_id(db)
                elif sub_choice == '3':
                    create_instructor(db)
                elif sub_choice == '0':
                    break
                else:
                    print("Invalid choice.")
        
        elif choice == '2':
            while True:
                print("\n--- Student Menu ---")
                print("1. List all students")
                print("2. Create new student")
                print("3. Delete student")
                print("0. Back to main menu")
                sub_choice = input("> ")
                if sub_choice == '1':
                    list_students(db)
                elif sub_choice == '2':
                    create_student(db)
                elif sub_choice == '3':
                    delete_student(db)
                elif sub_choice == '0':
                    break
                else:
                    print("Invalid choice.")
        
        elif choice == '3':
            while True:
                print("\n--- Course Menu ---")
                print("1. List all courses")
                print("2. Find course by name")
                print("3. Update course")
                print("0. Back to main menu")
                sub_choice = input("> ")
                if sub_choice == '1':
                    list_courses(db)
                elif sub_choice == '2':
                    find_course_by_name(db)
                elif sub_choice == '3':
                    update_course(db)
                elif sub_choice == '0':
                    break
                else:
                    print("Invalid choice.")

        elif choice == '0':
            exit_program()
        else:
            print("Invalid choice. Please try again.")