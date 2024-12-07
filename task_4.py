# Создать базовый класс Employer (служащий) с функцией Print(). Она должна выводить информацию о служащем. В случае базового класса это может быть строка
# Создайте от него три производных класса: President,
# Manager, Worker. Переопределите функцию Print() для
# вывода информации, соответствующей каждому типу
# служащего.

class Employer:
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def employer_print(self):
        return print("This is Employer class")
    
    def display(self):
        print(f'Name is {self.__name}')
        print(f'Surname is {self.__surname}')
        print(f'Age is {self.__age}')
    
    

class Worker(Employer):
    def __init__(self,name,surname,age):
        super().__init__(name,surname,age)
        
    def worker_print(self):
        return print("This is Worker class")
    
    def display(self):
        super().display()


class Manager(Employer):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def manager_print(self):
        return print('This is Manager class')

    def display(self):
        super().display()


class President(Employer):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def president_print(self):
        return print("This is President class")

    def display(self):
        super().display()

employer = Employer('John','Doe',25)
worker = Worker('Clint','Eastwood',90)
manager = Manager('Steve','Jobs',45)
president = President('Vladimir','Putin',72)

employer.employer_print()
employer.display()
print()
worker.worker_print()
worker.display()
print()
manager.manager_print()
manager.display()
print()
president.president_print()
president.display()