class Shape:
    def draw(self):
        print("Drawing Shape")
        
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")
        
d1=Circle()
d1.draw()        