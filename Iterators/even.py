class mynumbers:
    def __iter__(self):
        self.a =2
        return self
    
    def __next__(self):
        if self.a <=20:
            x=self.a
            self.a +=2
            return x
        else:
            raise StopIteration
        
myclass =mynumbers()
myiter= iter(myclass)

for x in myiter:
    print(x)  
