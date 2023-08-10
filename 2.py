"""
 Створіть клас Animal. Також створіть екземпляр класу Animal та привласніть змінній animal. 
 Для класу Animal у конструкторі створіть дві властивості: nickname - кличка тварини та weight - вага тварини. 
 Реалізуйте також метод класу say. 
 При реалізації методу можна використати оператор pass, поки що головне - це визначення, а не конкретна реалізація.
 
	"""

class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
    
    def say(self):
        pass

# Створення екземпляру класу Animal
animal = Animal("Барсик", 5.2)

# Виведення деякої інформації про тварину
print(f"Кличка: {animal.nickname}")
print(f"Вага: {animal.weight} кг")