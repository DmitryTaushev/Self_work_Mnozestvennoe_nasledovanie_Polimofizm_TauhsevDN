# Создать базовый класс «Домашнее животное» и производные классы«Собака», «Кошка», «Попугай», «Хомяк».
# С помощью конструктора установить имя каждого животного и его характеристики. Реализуйте для каждого
# из классов методы:
# ■ Sound — издает звук животного (пишем текстом в
# консоль);
# ■ Show — отображает имя животного;
# ■ Type — отображает название его подвида;

class HomeAnimal:
    def __init__(self,name,typ):
        self.name = name
        self.typ = typ


class Dog(HomeAnimal):
    
    def __init__(self,name,typ,ani_sound):
        super().__init__(name,typ)
        self.ani_sound = ani_sound
    def animal_sound(self):
        return print(f"Животное издает звуки {self.ani_sound}")


    def show(self):
        return print(f'Имя животного {self.name}')

    def type_animal(self):
        return print(f"Подвид животного {self.typ}")

sound = input('Введите звук который издают собаки')
dog = Dog("Тузик","Собака",f'{sound}')
dog.show()
dog.type_animal()
dog.animal_sound()


class Cat(HomeAnimal):

    def __init__(self, name, typ, ani_sound):
        super().__init__(name, typ)
        self.ani_sound = ani_sound

    def animal_sound(self):
        return print(f"Животное издает звуки {self.ani_sound}")

    def show(self):
        return print(f'Имя животного {self.name}')

    def type_animal(self):
        return print(f"Подвид животного {self.typ}")


sound = input('Введите звук которое издает кошка')
cat = Cat("Барсик", "Кошка", f'{sound}')
cat.show()
cat.type_animal()
cat.animal_sound()

class Parrot(HomeAnimal):

    def __init__(self, name, typ, ani_sound):
        super().__init__(name, typ)
        self.ani_sound = ani_sound

    def animal_sound(self):
        return print(f"Животное издает звуки {self.ani_sound}")

    def show(self):
        return print(f'Имя животного {self.name}')

    def type_animal(self):
        return print(f"Подвид животного {self.typ}")


sound = input('Введите звук который издает попугай')
parrot = Parrot("Кеша", "Попугай", f'{sound}')
parrot.show()
parrot.type_animal()
parrot.animal_sound()

class Hamster(HomeAnimal):

    def __init__(self, name, typ, ani_sound):
        super().__init__(name, typ)
        self.ani_sound = ani_sound

    def animal_sound(self):
        return print(f"Животное издает звуки {self.ani_sound}")

    def show(self):
        return print(f'Имя животного {self.name}')

    def type_animal(self):
        return print(f"Подвид животного {self.typ}")


sound = input('Введите звук который издает хомяк')
hamster = Hamster("Хома", "Хомяк", f'{sound}')
hamster.show()
hamster.type_animal()
hamster.animal_sound()


