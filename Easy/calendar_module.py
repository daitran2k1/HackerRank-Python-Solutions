import calendar

days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

if __name__ == "__main__":
    month, day, year = map(int, input().split())
    day_of_week = calendar.weekday(year, month, day)
    print(days[day_of_week])
