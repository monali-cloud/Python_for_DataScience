#Create a parent class Employee with a method work().
#Create child classes:
#Developer,Tester,Manager
#Each class should override work().
#Create objects of all three classes and call work() using a loop.

class Employee:
    def work(self):
        print("employee is working")
    
class Developer(Employee):
    def work(self):
      print("developer is writing code")
        
class tester(Employee):
    def work(self):          
       print("Testing Software")
       
class manager(Employee):
    def work(self):
        print("managing the team")
        
Employees =[Developer(),tester(),manager()]

for emp in Employees:
    emp.work()               