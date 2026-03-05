import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності параметрів
    if min < 1 or max > 1000 or min > max:
        return []
    
    if quantity > (max - min + 1) or quantity < 1:
        return []

    # Генеруємо унікальні випадкові числа
    numbers = random.sample(range(min, max + 1), quantity)

    # Сортуємо список
    numbers.sort()

    return numbers


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)