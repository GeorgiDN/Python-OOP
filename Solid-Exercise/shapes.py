from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calc_area(self):
        pass


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calc_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calc_area(self):
        return (self.base * self.height) / 2


class Square(Shape):
    def __init__(self, base):
        self.base = base

    def calc_area(self):
        return self.base ** 2


class AreaCalculator:
    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calc_area()

        return total


# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)



# Condition
# You are provided with code containing class Rectangle and class AreaCalculator.
# Refactor the code using the Open/Closed Principle so that the code is open
# for extension (adding more shapes) but closed for modification.


#Code for edit
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
# class AreaCalculator:
#
#     def __init__(self, shapes):
#
#         assert isinstance(shapes, list), "`shapes` should be of type `list`."
#         self.shapes = shapes
#
#     @property
#     def total_area(self):
#         total = 0
#         for shape in self.shapes:
#             total += shape.width * shape.height
#
#         return total
#
#
# shapes = [Rectangle(2, 3), Rectangle(1, 6)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)