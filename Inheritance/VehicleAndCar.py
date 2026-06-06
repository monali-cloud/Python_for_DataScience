#Create a parent class Vehicle with attributes brand and year.
#Create a child class Car that adds an attribute model.
#Create an object:

class Vehicle:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year
        
        
class Car(Vehicle):
    def __init__(self, brand, year, model) :
        super().__init__(brand,year)
        self.model=model 
        
    def display(self):
        print("Brand : ",self.brand)
        print("year :",self.year)
        print("Model :",self.model)
        
        
c1=Car("Totota",2023,"Corolla")
c1.display()                      
        