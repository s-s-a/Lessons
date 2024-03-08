""" Эксперименты с DatTime """

import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.datetime.now().time())

print(datetime.time(10, 30, 11))
print(datetime.date(2023, 2, 11))
print(datetime.datetime(2023, 2, 11))
print(datetime.datetime(2023, 2, 11, 10, 30, 11))

print(datetime.timedelta(days=5, seconds=5, microseconds=4, milliseconds=1, minutes=10, hours=2, weeks=5))
print(datetime.datetime.today() - datetime.timedelta(days=7))
print(datetime.datetime.today() + datetime.timedelta(weeks=4))

print(datetime.datetime.strptime('06.02.23 12:06:58', '%d.%m.%y %H:%M:%S'))
print(datetime.datetime.strptime('06.02.2023 12:06:58', '%d.%m.%Y %H:%M:%S'))
print(datetime.datetime.strptime('06-02-2023 12:06:58', '%d-%m-%Y %H:%M:%S'))
print(datetime.datetime.strptime('Monday, 06 April 2023 12:06:58', '%A, %d %B %Y %H:%M:%S'))

print(datetime.date(2023, 3, 1) - datetime.date(2023, 1, 31))