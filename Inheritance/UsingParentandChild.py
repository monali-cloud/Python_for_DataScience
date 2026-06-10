class Employee:
    def __init__(self,name):
        self.name=name
        
    def display_name(self):
        print(self.name)
        
class Manager(Employee):
    def work(self):
        print("Managing Team")
     
class staff(Employee):
    def work(self):
        print(f"staff : {self.name}")        
m1=Manager("John")     
m1.work()   
m1.display_name()

m2=staff("Emi")
m1.work()
m2.work()


m1.work()
m1.display_name()
m2.work()



        
    
        