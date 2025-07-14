class car:
    def __init__(self,brand, model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display(self):
        print(f"car:{self.brand} {self.model}  {self.year} ")    
    


my_car=car("Toyta","Corolla",2020)
my_car.display()
 
        