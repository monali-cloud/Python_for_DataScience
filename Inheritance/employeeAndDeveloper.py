#Create a parent class Employee with attributes name and salary.
#Create a child class Developer that inherits from Employee and adds an attribute language.
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        
        
class Developer(Employee):
    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language= language
        
        
        
    def display(self):
        print("Name :",self.name)
        print("salary : ",self.salary)
        print("Language:",self.language)    
        
d1=Developer("john","50000","python") 
d1.display()       