# Для классов из задания 4 реализуйте магический
# метод str, а также метод int (должен возвращать возраст
# служащего).

class Employer:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.age = age

    def __str__(self):
        return print("This is Employer class")

    def display(self):
        print(f'Name is {self.__name}')
        print(f'Surname is {self.__surname}')

    def __int__(self):
        print(f'Age is {self.age}')



class Worker(Employer):
    def __init__(self, name, surname,age):
        super().__init__(name, surname,age)

    def __str__(self):
        return print("This is Worker class")

    def display(self):
        super().display()

    def __int__(self):
        print(f'Age is {self.age}')


class Manager(Employer):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__(self):
        return print('This is Manager class')

    def display(self):
        super().display()

    def __int__(self):
        print(f'Age is {self.age}')


class President(Employer):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def __str__(self):
        return print("This is President class")

    def display(self):
        super().display()

    def __int__(self):
        print(f'Age is {self.age}')


employer = Employer('John', 'Doe', 25)
worker = Worker('Clint', 'Eastwood', 90)
manager = Manager('Steve', 'Jobs', 45)
president = President('Vladimir', 'Putin', 72)

employer.__str__()
employer.display()
employer.__int__()
print()
worker.__str__()
worker.display()
worker.__int__()
print()
manager.__str__()
manager.display()
manager.__int__()
print()
president.__str__()
president.display()
president.__int__()