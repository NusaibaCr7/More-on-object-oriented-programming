class Circle:
    def __init__(self,r):
        self.r = r
    
    def area(self):
        return (3.1416)*(self.r**2)

    def perimeter(self):
        return 2*(3.1416)*(self.r)
    
radius = float(input("Enter the radius: "))
c1 = Circle(radius)
print(f"Area of the circle: {c1.area()}")
print(f"Perimeter of the circle: {c1.perimeter()} ")
