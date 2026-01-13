import json
import os

FILE_NAME = "student-data.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

def add_student():
    students = load_data()
    student = {
        "name": input("Enter Name: "),
        "gender": input("Enter Gender (Male/Female): "),
        "physics": int(input("Enter Physics Marks: ")),
        "maths": int(input("Enter Maths Marks: ")),
    }
    students.append(student)
    save_data(students)
    print("Student added successfully!")

def view_students():
    students = load_data()
    if not students:
        print("No students found.")
        return
    for s in students:
        print(s)

def update_student():
    students = load_data()
    name_to_update = input("Enter student name to update: ")

    for s in students:
        if s["name"].lower() == name_to_update.lower():
            print("Enter new details (leave blank to keep old value)")

            new_name = input(f"New name ({s['name']}): ")
            new_gender = input(f"New gender ({s['gender']}): ")
            new_physics = input(f"New physics marks ({s['physics']}): ")
            new_maths = input(f"New maths marks ({s['maths']}): ")
            new_english = input(f"New english marks ({s['english']}): ")

            if new_name:
                s["name"] = new_name
            if new_gender:
                s["gender"] = new_gender
            if new_physics:
                s["physics"] = int(new_physics)
            if new_maths:
                s["maths"] = int(new_maths)
            if new_english:
                s["english"] = int(new_english)

            save_data(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student():
    students = load_data()
    name_to_delete = input("Enter student name to delete: ")


    new_students = [
        s for s in students
        if s["name"].lower() != name_to_delete.lower()
    ]

    if len(new_students) == len(students):
        print("Student not found.")
    else:
        save_data(new_students)
        print("Student deleted successfully!")

def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

menu()