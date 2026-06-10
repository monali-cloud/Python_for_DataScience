class Animal:
    def __init__(self,name):
        self.name=name
        
class Dog(Animal):
    def bark(self):
        print(f"{self.name} says Woof!")      
        
d1=Dog("Buddy")

d1.bark()          