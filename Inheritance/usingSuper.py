class person:
    def __init__(self,name):
        self.name=name
        
class Student(person):
    def __init__(self,name, roll_no):
        super().__init__(name)
        self.roll_no=roll_no        
                
                
    def display(self):
        print("name:",self.name)
        print("Roll no:",self.roll_no)
        
                      
s1=Student("Mike",32)

s1.display()             