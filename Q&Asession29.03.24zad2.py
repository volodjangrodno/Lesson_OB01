# Задача 2
# Цель задания: Изучение концепций классов и объектов на примере геометрической фигуры.
# Инструкция: Создайте класс Треугольник.
# В инициализаторе класса определите три атрибута: сторона1, сторона2 и сторона3, представляющие стороны треугольника.
# Создайте метод периметр, который возвращает периметр треугольника.
# Дополнительно, можете создать метод тип, который будет определять,
# является ли треугольник равносторонним, равнобедренным или разносторонним.

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def type(self):
        if self.side1 == self.side2 == self.side3:
            return "равносторонний"
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            return "равнобедренный"
        else:
            return "разносторонний"

triangle1 = Triangle(3, 4, 4)
triangle2 = Triangle(6, 6, 6)
triangle3 = Triangle(3, 4, 5)

print(
    f"Периметр треугольника 1: {triangle1.perimeter()}\n"
    f"Тип треугольника 1: {triangle1.type()}\n"
)

print(
    f"Периметр треугольника 2: {triangle2.perimeter()}\n"
    f"Тип треугольника 2: {triangle2.type()}\n"
)

print(
    f"Периметр треугольника 3: {triangle3.perimeter()}\n"
    f"Тип треугольника 3: {triangle3.type()}\n"
)