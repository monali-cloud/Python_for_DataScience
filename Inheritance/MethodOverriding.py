class Animal:
    def speak(self):
        print("Animal Sound")
        
        
class Dog(Animal):
    def speak(self):
       print("Woof!!")
    
d1=Dog()
d2=Animal()

d2.speak()
d1.speak()            
        