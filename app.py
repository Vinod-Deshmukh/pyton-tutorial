print("#39 Classes")
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

point1=Point()
point1.draw()
point1.move()
point1.x=100
point1.y=250
print(point1.y)
point2=Point()
point2.y=7500000000
print(point2.y)