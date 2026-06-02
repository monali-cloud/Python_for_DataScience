class mynumbers:
    def __init__(self):
        self.a =5
        
    def __iter__(self):
        return self
    
    def __next__(self):
        x=self.a
        self.a -=1
        return x
    
myclass = mynumbers()
myiter=iter(myclass)
    
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))