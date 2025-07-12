class Student:
    def __init__(self,name, age):
        self.name=name
        self.age=age

    def show(self):
        print("This is ",self.name)

s1=Student("Rayhan",22)
s2=Student("saif",24)
s1.show()
s2.show()