from datetime import datetime

current_datetime = datetime.now()
print("Текущая дата и время:", current_datetime)

current_year = current_datetime.year
print("Текущий год:", current_year)

current_month = current_datetime.strftime("%B")
print("Месяц года:", current_month)

week_number = current_datetime.strftime("%U")
print("Номер недели в году:", week_number)

weekday = current_datetime.strftime("%A")
print("Будний день недели:", weekday)

day_of_year = current_datetime.timetuple().tm_yday
print("День года:", day_of_year)

day_of_month = current_datetime.day
print("День месяца:", day_of_month)

day_of_week = current_datetime.weekday()
print("День недели (0 - понедельник, 6 - воскресенье):", day_of_week)

#######################################################################

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input("Введите год: "))

if is_leap_year(year):
    print(f"{year} - високосный год.")
else:
    print(f"{year} - не високосный год.")

##############################################

input_date_str = "1 января 2014 14:43"

months = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}

parts = input_date_str.split()

day = int(parts[0])
month_str = parts[1]
year = int(parts[2])
time_str = parts[3]

month = months[month_str]

formatted_date_str = f"{year:04d}-{month:02d}-{day:02d} {time_str}:00"
formatted_date = datetime.strptime(formatted_date_str, "%Y-%m-%d %H:%M:%S")

print(formatted_date.strftime("%Y-%m-%d %H:%M:%S"))

####################################################

current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S.%f")
print(formatted_time)
