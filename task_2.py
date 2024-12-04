#Используя механизм множественного наследования
#разработайте класс “Автомобиль”. Должны быть классы
#«Колеса», «Двигатель», «Двери» и т.д.

class Wheels:

    def __init__(self,wheels):
        self.__wheels = wheels

    def display(self):
        print(f'Колеса марки {self.__wheels}')

    def get_wheels(self):
        return self.__wheels

class Engine(Wheels):
    def __init__(self,wheels,engine):
        super().__init__(wheels)
        self.__engine = engine

    def display(self):
        super().display()
        print(f'Двигатель объемом {self.__engine}')

    def get_engine(self):
        return self.__engine

class Doors(Engine):
    def __init__(self,wheels,engine,doors):
        super().__init__(wheels,engine)
        self.__doors = doors

    def display(self):
        super().display()
        print(f'Количество дверей {self.__doors}')

    def get_doors(self):
        return self.__doors

class Car(Doors):

    def __init__(self, wheels, engine, doors, model):
        super().__init__(wheels,engine,doors)
        self.__model = model

    def display(self):
        super().display()
        print(f"Модель машины {self.__model}")

car = Car('Gislaved',"1,8L",'4',"Toyota")

car.display()





