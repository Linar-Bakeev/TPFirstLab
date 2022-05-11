import numbers


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x, self.y == other.x, other.y

    def __ne__(self, other):
        if self.x == other.x and self.y == other.y:
            return False
        return True

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            self.x *= other
            self.y *= other
            return self
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


p1 = Point(1, 2)
p2 = Point(5, 6)

if p1 == p2:
    print("Equal True")
else:
    print("Equal False")

if p1 != p2:
    print("Not equal True")
else:
    print("Not equal False")

