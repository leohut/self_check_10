"""
Створіть клас IDException, який успадковуватиме клас Exception.

Також реалізуйте функцію add_id(id_list, employee_id), 
яка додає до списку id_list ідентифікатор користувача employee_id та повертає вказаний оновлений список id_list.

Функція add_id буде викликати власне виключення IDException, 
якщо employee_id не починається з '01', інакше employee_id буде додано до списку id_list.    
    
"""


class IDException(Exception):
    pass

def add_id(id_list, employee_id):
    if employee_id.startswith('01'):
        id_list.append(employee_id)
        return id_list
    else:
        raise IDException(f"Invalid employee ID: {employee_id}")

# Приклад використання
try:
    ids = []
    ids = add_id(ids, '012345')
    print(ids)  # Вивід: ['012345']
    
    ids = add_id(ids, '234567')
    print(ids)  # Вивід: ['012345', '234567']
    
    ids = add_id(ids, '987654')  # Викидає виключення IDException
except IDException as e:
    print(f"Caught an IDException: {e}")