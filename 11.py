"""
Створіть клас NumberString, успадкуйте його від класу UserString, 
визначте для нього метод number_count(self), 
який буде рахувати кількість цифр у рядку.    
    
"""


from collections import UserString

class NumberString(UserString):
    def number_count(self):
        count = 0
        for char in self.data:
            if char.isdigit():
                count += 1
        return count

# Приклад використання
string_with_numbers = NumberString("Hello12345")
print(string_with_numbers.number_count())  # Виведе 5, оскільки у рядку "Hello12345" є 5 цифр