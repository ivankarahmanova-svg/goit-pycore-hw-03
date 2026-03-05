from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        # Перетворюємо рядок у дату
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        
        # Поточна дата
        today = datetime.today().date()
        
        # Різниця між датами
        difference = today - given_date
        
        return difference.days

    except ValueError:
        print("Невірний формат дати. Використовуйте формат YYYY-MM-DD.")
        return None


# Приклад використання
print(get_days_from_today("2023-10-09"))