import datetime

today = datetime.date.today()

start = datetime.date(2017, 12, 30)

increment = datetime.timedelta(days = 3)

numOfCharts = (today - start) / increment

print(start)

print(numOfCharts)