
import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(self._initialize_sides(sides))
        self.__color = list(color)
        self.filled = False

    @staticmethod
    def __is_valid_color(r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_color(self):
        return self.__color

    @staticmethod
    def __is_valid_sides(*new_sides):
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def _initialize_sides(self, sides):
        if len(sides) == 0 or not self.__is_valid_sides(*sides):
            return [1] * self.sides_count
        return sides

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius <strong> 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        # Heron's formula for area of triangle
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color, *([edge_length] * self.sides_count))

    def get_volume(self):
        edge = self.get_sides()[0]
        return edge**3  # Volume of cube = edge^3

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

# Проверка периметра
print(len(circle1))

# Проверка объёма
print(cube1.get_volume())




