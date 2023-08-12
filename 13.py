"""
Як ми вже говорили, поліморфізм - це здатність програми вибирати різні реалізації 
при виклику операцій з однією і тією ж назвою.

Але поліморфізм - це також здатність об'єктів прикидатись чимось іншим. 
У наведеному вище прикладі Chupakabra прикидалася собакою та кішкою.

Для коду із завдання вам необхідно реалізувати клас CatDog, 
не використовуючи успадкування від класу Animal, 
але щоб екземпляр класу CatDog поводився як і, 
як екземпляр класу Cat, тобто. він повинен вдати, що він клас Cat.   
    
"""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight


class Cat(Animal):
    def say(self):
        return "Meow"


class CatDog:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
        self.cat = Cat(nickname, weight)

    def say(self):
        return self.cat.say()

    def change_weight(self, weight):
        self.cat.change_weight(weight)

# Приклад використання
cd = CatDog("Fido", 10)
print(cd.say())  # Виведе: "Meow"
print(cd.nickname)  # Виведе: "Fido"
cd.change_weight(15)