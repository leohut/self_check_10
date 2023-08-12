"""
Створіть два класи: CatDog та DogCat. Ці класи повинні наслідуватись від двох класів відразу: Cat та Dog. 
Після успадкування в екземпляра класу CatDog, батьківський метод say повинен повертати "Meow", 
а у класу DogCat — "Woof". Для обох зазначених класів реалізуйте метод info, 
який повертає рядок у наступному форматі f"{self.nickname}-{self.weight}".

"""


class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


class Cat(Animal):
    def say(self):
        return "Meow"


class Dog(Animal):
    def say(self):
        return "Woof"


class CatDog(Cat, Dog):
    def __init__(self, nickname, weight):
        super().__init__(nickname, weight)

    def say(self):
        return "Meow"

    def info(self):
        return f"{self.nickname}-{self.weight}"


class DogCat(Dog, Cat):
    def __init__(self, nickname, weight):
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def info(self):
        return f"{self.nickname}-{self.weight}"
    