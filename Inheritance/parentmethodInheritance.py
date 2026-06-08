class person:
    def __init__(self,name):
        self.name=name
        
    def introduce(self):
        print(f"My name is {self.name}")
        
class Student(person):
    pass

s1=Student("Monali")

s1.introduce()        
        
        
            