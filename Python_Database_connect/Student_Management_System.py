import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="myapp"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        course VARCHAR(255)
    )
""")

def insert_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    query = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, course))
    db.commit()
    print(" Student added successfully!")

def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    print("\n All Students:")
    for row in result:
        print(row)

def update_student():
    student_id = input("Enter Student ID to update: ")
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    course = input("Enter new course: ")
    query = "UPDATE students SET name=%s, age=%s, course=%s WHERE id=%s"
    cursor.execute(query, (name, age, course, student_id))
    db.commit()
    print(" Student updated successfully!")

def delete_student():
    student_id = input("Enter Student ID to delete: ")
    query = "DELETE FROM students WHERE id=%s"
    cursor.execute(query, (student_id,))
    db.commit()
    print(" Student deleted successfully!")

def menu():
    while True:
        print("\n Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            insert_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print(" Exiting program...")
            break
        else:
            print(" Invalid choice! Please try again.")

menu()
cursor.close()
db.close()
