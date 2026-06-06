class Solve:
    def create(self,a,b):
        self.a=a
        self.b=b
        print("Answers : ")
    
class add(Solve):
        def addition(self,a,b):
            self.create(a,b)
            print(f"Addition of a and b is :",self.a + self.b)
        
class sub(Solve):
    def subtraction(self,a,b):
        self.create(a,b)
        print(f"Subtraction is : ",self.a - self.b)
        
d1=add()
d1.addition(10,2)                

d2=sub()
d2.subtraction(10, 2)