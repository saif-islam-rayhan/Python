class Animal:
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

a = Animal()
d = Dog()
c = Cat()

a.speak()   
d.speak()   
c.speak()   
