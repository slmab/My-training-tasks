# TODO здесь писать код

class Circle:
    pi = 3.14

    def __init__(self, x_center=0, y_center=0, radius=1):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

    def perimeter(self):
        return self.pi * self.radius * 2

    def scale(self, k):
        self.radius = self.radius * k
        return self.radius

    def intersect(self, x, y, r):
        distance = ((self.x_center - x) ** 2 +
                    (self.y_center - y) ** 2) ** 0.5
        if distance < self.radius + r:
            print('Окружности пересекаются.')
        else:
            print('Окружности не пересекаются.')


circle_1 = Circle()
print('Площадь круга:', circle_1.area())
print('Периметр круга:', circle_1.perimeter())
print('Новый радиус круга', circle_1.scale(5))
circle_1.intersect(0, 2, 2)
