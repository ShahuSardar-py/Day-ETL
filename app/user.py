from app.etl import run_daily_el
from datetime import date

def get_float(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError
            if max_val is not None and value > max_val:
                raise ValueError
            return value
        except ValueError:
            print("Enter a valid number.")

def get_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                raise ValueError
            if max_val is not None and value > max_val:
                raise ValueError
            return value
        except ValueError:
            print("Enter a valid integer.")

def main():
    print("\n📘 Daily Life Logger\n")

    log = {
        "log_date": date.today().strftime("%Y-%m-%d"),
        "sleep_hours": get_float("Sleep hours: ", 0, 24),
        "sleep_quality": get_int("Sleep quality (1–5): ", 1, 5),
        "mood_rate": get_int("Mood (1–5): ", 1, 5),
        "focus_hours": get_float("Focused work hours: ", 0, 16),
        "notes": input("Notes (optional): ")
    }

    run_daily_el(log)

    print("\n✅ Day logged successfully.")
    print(f"📅 Date: {log['log_date']}")

if __name__ == "__main__":
    main()
