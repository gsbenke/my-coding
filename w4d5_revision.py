#creating class
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Coords {self.x}, {self.y}"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        point3 = Point2D(x,y)
        return point3

def point_adder(point1, point2):
    x = point1.x + point2.x
    y = point1.y + point2.y
    point3 = Point2D(x, y)
    return point3

point1 = Point2D(10, 1)
print(point1)
str_point1 = str(point1)

point2 = Point2D(1, 2)
print(point2)
str_point2 = str(point2)

new_point = point_adder(point1, point2)
print(new_point)
str_new_point = str(new_point)

new_point2 = point1 + point2
                