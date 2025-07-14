class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self, name, student_id):
        super().__init__(name)        
        self.student_id = student_id

    def show_id(self):
        print(f"My ID is {self.student_id}")

s = Student("Rayhan", 101)
s.show()     
s.show_id()    
