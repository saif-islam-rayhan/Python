class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Salary: {self.salary}")


class Manager(Employee):
    def display_info(self):
        super().display_info()
        print("Role: Manager")


class Developer(Employee):
    def display_info(self):
        super().display_info()
        print("Role: Developer")


e1 = Manager("Rayhan", 101, 70000)
e2 = Developer("Asha", 102, 50000)

e1.display_info()
print("-----")
e2.display_info()
