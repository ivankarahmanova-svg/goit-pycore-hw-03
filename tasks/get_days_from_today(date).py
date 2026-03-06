from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = today - given_date
        return difference.days
    except ValueError:
        print("Невірний формат дати. Використовуйте формат YYYY-MM-DD.")
        return None


if __name__ == "__main__":
    print(get_days_from_today("2023-10-09"))