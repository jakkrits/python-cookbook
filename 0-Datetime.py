import datetime

d = datetime.date(2018, 3, 28)
print(d)

todays_date = datetime.date.today()
print(todays_date)
print(todays_date.weekday())
print(todays_date.isocalendar())
print(todays_date.ctime())
print(todays_date.isoweekday())

# weekday - monday 0
# isoweekday - monday 1

tdelta = datetime.timedelta(days=7)
print(todays_date + tdelta)

print(todays_date - tdelta)