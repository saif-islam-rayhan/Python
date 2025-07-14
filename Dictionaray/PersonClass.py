class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def isadelt(self):
        if self.age>18:
            print(f"{self.name} is a addelt person. because {self.age} years old")
p1=Person("Busra",5)
p2=Person("Saimun",26)
p3=Person("Rafi",14)

