import calendar
import datetime

print(datetime.datetime.now())
calender = int(input("Input the year: "))
calender2 = int(input("Input the month: "))

print(calendar.month(calender, calender2))