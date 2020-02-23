import copy


# ------------------TASK1--- 7 variant
class Book:
    def __init__(self):
        self.id = 0
        self.title = "book"
        self.authors = []
        self.publishers = "publishers"
        self.year = "2020"
        self.pages = 0
        self.price = 0
        self.cover = "hard"
        print("new Book object created with default constructor")

    def __init__(self, i, tit, au, pub, y, pag, pri, cov):
        self.id = i
        self.title = tit
        self.authors = []
        self.authors.append(au)
        self.publishers = pub
        self.year = y
        self.pages = pag
        self.price = pri
        self.cover = cov
        print("new Book object created with parameterized constructor")

    def __setattr__(self, key, value):
        if key == "id" or key == "title" or key == "price" or key == "publishers" or key == "cover" or key == "pages" or key == "year" or key == "authors":
            self.__dict__[key] = value
        else:
            raise AttributeError

    def __str__(self):
        return "id: {0}\ntitle:{1}\nauthors:{2}\nyear:{3}".format(self.id, self.title, self.authors, self.year)

    def get_id(self):
        return self.id

    def set_price(self, p):
        if p < 0:
            print("price must be positive")
        else:
            self.price = p


library = [
    Book(1, "Война и Мир", "Толстой", "Русский вестник", "1865", 1021, 3, "твёрдая"),
    Book(2, "Тихий Дон", "Шолохов", "Ростиздат", "1939", 721, 2.5, "твёрдая"),
    Book(3, "Воскресение", "Толстой", "Нива", "1899", 444, 0.5, "мягкая"),
    Book(4, "Евгений Онегин", "Пушкин", "Типография Глазунова", "1825", 102, 2, "мягкая"),
    Book(5, "Поднятая целина", "Шолохов", "Новый мир", "1932", 498, 2.4, "мягкая"),
    Book(6, "Горе от ума", "Грибоедов", "Русский вестник", "1825", 45, 2, "твёрдая"),
]
author = input("искать автора: ")
a_found = []
for b in library:
    for a in b.authors:
        if a == author:
            a_found.append(b)
if len(a_found) != 0:
    for a in a_found:
        print(a)
else:
    print("книг не найдено")
years = int(input("искать выпущенные после: "))
y_found = []
for b in library:
    if int(b.year) >= years:
        y_found.append(b)
if len(y_found) != 0:
    for a in y_found:
        print(a)
else:
    print("книг не найдено")


# ----------TASK2--- 11 variant
class Transport:
    def __init__(self, pas, speed):
        self.passengers = pas
        self.speed = speed

    def __str__(self):
        return "passengers: {0}\naverage speed: {1}".format(self.passengers, self.speed)


class Engine:
    def __init__(self, power, litres, what_for):
        self.power = power
        self.litres = litres
        self.what_for = what_for


class Wagon:
    def __init__(self, floors, seats):
        self.floors = floors
        self.seats = seats


class Car(Transport):
    def __init__(self, pas, speed, engine, mark, color):
        Transport.__init__(self, pas, speed)
        self.mark = mark
        self.color = color
        self.engine = copy.copy(engine)

    def __str__(self):
        return "{0}-colored car, average speed - {1}".format(self.color, self.speed)


class Train(Transport):
    def __init__(self,  pas, speed, engine, mechanic, wagons, dep):
        Transport.__init__(self, pas, speed)
        self.mechanic = mechanic
        self.engine = copy.copy(engine)
        self.depo = dep
        self.wagons = list()
        self.wagons.append(wagons)

    def __str__(self):
        return "trains mechanic - {0}, wagons amount - {1}".format(self.mechanic, len(self.wagons[0]))


class Express(Train):
    def __init__(self, engine, pas, speed, mechanic, wagons, dep, has_rest):
        Train.__init__(self, engine, pas, speed, mechanic, wagons, dep)
        self.has_restaurant = has_rest

    def __str__(self):
        return "express mechanic - {0}, wagons amount - {1}".format(self.mechanic, len(self.wagons[0]))


car_engine = Engine(150, 1.6, "car")
train_engine = Engine(350000, 5000, "train")
train_wagons = [
    Wagon(2, 100),
    Wagon(1, 50),
    Wagon(2, 150),
    Wagon(1, 40)
]
transport = Transport(300, 100)
train = Train(390, 110, train_engine, "Vasek", train_wagons, "Minsk")
express = Express(train_engine, 390, 150, "Vitek", train_wagons, "Minsk", True)
car = Car(4, 200, car_engine, "ford", "pink")
print("-------------------")
print(transport)
print(car)
print(train)
print(express)
