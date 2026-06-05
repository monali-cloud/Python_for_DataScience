class vehicle:
    def __init__(self,brand):
        self.brand=brand
        
    def show_brand(self):
        print(self.brand)
        
class Car(vehicle):
    pass

c1 =Car("Toyota")
c1.show_brand()            
