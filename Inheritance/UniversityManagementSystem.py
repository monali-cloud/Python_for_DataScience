#Create a parent class Person with:
#name,age
#Create a child class Professor with:
#subject,salary
#Display all details of the professor.

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
        
class professor(person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.subject=subject
        self.salary= salary 
        
    def display(self):
        print("name :",self.name)
        print("Age:",self.age)
        print("Subject:",self.subject)
        print("Salary :",self.salary)
                   
p1=professor("John",32,"Python",50000)
p1.display()                   
                   