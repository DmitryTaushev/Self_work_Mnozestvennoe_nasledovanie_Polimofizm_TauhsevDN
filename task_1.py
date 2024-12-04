#Используя понятие множественного наследования,
#разработайте класс «Окружность, вписанная в квадрат».
from math import pi
class Square:

    def __init__(self,length_square):
        self.__length_square = length_square

    def display(self):
        print(f'Длина стороны квадрата = {self.__length_square}')
        print(f'Площадь квадрата = {self.__length_square ** 2}')
        print(f'Периметр квадрата = {self.__length_square * 4}')

    def get_length_square(self):
        return self.__length_square


class Circle(Square):

    def __init__(self,length_square):
        super().__init__(length_square)
        diameter = length_square
        self.__diameter = diameter

    def display(self):
        print(f'Диаметр окружности = {self.__diameter}')
        print(f'Длина окружности = {self.__diameter * pi}')
        print(f'Площадь окружности = {((self.__diameter/2)**2) * pi}')

    def get_diameter(self):
        return self.__diameter

all_length = 5
square = Square(all_length)
circle = Circle(all_length)

square.display()
print()
circle.display()





