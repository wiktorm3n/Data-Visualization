import csv
import matplotlib.pyplot as plt
from datetime import date, datetime

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    '''Get dates, and rainfall from this file'''
    dates,rainfall  = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        rain = float(row[3])
        dates.append(current_date)
        rainfall.append(rain)

'''Plot rainfall '''
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rainfall, c='red', alpha=0.5)
plt.fill_between(dates, rainfall, facecolor='blue', alpha=0.1)

'''Format plot'''
plt.title("Daily rainfall(ml/cm2 ?) - 2018", fontsize=24)
plt.xlabel(" ", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rainfall ", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
