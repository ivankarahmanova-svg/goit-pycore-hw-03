from datetime import datetime, date, timedelta


def get_birthday_this_year(birthday_date: date, year: int) -> date:
    try:
        return birthday_date.replace(year=year)
    except ValueError:
        return date(year, 3, 1)


def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    today: date = datetime.today().date()
    end_date: date = today + timedelta(days=7)
    result: list[dict[str, str]] = []

    for user in users:
        birthday_date: date = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()

        birthday_this_year: date = get_birthday_this_year(
            birthday_date,
            today.year
        )

        if birthday_this_year < today:
            birthday_this_year = get_birthday_this_year(
                birthday_date,
                today.year + 1
            )

        if today <= birthday_this_year <= end_date:
            congratulation_date: date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return result


if __name__ == "__main__":
    users: list[dict[str, str]] = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
    ]

    print(get_upcoming_birthdays(users))