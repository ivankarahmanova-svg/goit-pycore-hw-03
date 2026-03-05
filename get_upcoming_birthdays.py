from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    result = []

    for user in users:
        # 1) Перетворюємо день народження з рядка у дату
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # 2) Робимо день народження в цьому році
        birthday_this_year = birthday_date.replace(year=today.year)

        # 3) Якщо в цьому році вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # 4) Перевіряємо, чи потрапляє у проміжок "сьогодні ... 7 днів вперед"
        if today <= birthday_this_year <= end_date:
            congratulation_date = birthday_this_year

            # 5) Якщо день народження у вихідні — переносимо на понеділок
            # weekday(): 0=Пн, 5=Сб, 6=Нд
            if congratulation_date.weekday() == 5:      # субота
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:    # неділя
                congratulation_date += timedelta(days=1)

            # 6) Додаємо у результат
            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


# приклад
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
]

print(get_upcoming_birthdays(users))