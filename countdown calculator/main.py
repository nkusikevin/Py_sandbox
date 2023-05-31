
import datetime

def get_user_input():
    year = int(input("Enter the target year: "))
    month = int(input("Enter the target month: "))
    day = int(input("Enter the target day: "))
    target_date = datetime.date(year, month, day)
    return target_date

def calculate_countdown(target_date):
    current_date = datetime.date.today()
    time_left = target_date - current_date
    return time_left

def display_countdown(time_left):
    print("Countdown:")
    print("Days:", time_left.days)

def main():
    print("Welcome to the Countdown Calculator!")
    target_date = get_user_input()
    time_left = calculate_countdown(target_date)
    display_countdown(time_left)

if __name__ == "__main__":
    main()
