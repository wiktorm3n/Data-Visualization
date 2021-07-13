import csv
from datetime import date, datetime
import matplotlib.pyplot as plt

filename1 = 'data/death_valley_2018_simple.csv'
filename2 = 'data/sitka_weather_2018_simple.csv'
dates, highs, lows = [], [], []
with open(filename1) as f1:
    reader1 = csv.reader(f1)
    header_row = next(reader1)

    '''Get dates, and high and low temperatures from this file'''
    for row in reader1:
        current_date1 = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high1 = int(row[4])
            low1 = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date1}, filename1")
        else:
            dates.append(current_date1)
            highs.append(high1)
            lows.append(low1)

with open(filename2) as f2:
    reader2 = csv.reader(f2)
    header_row = next(reader2)

    for row in reader2:
        current_date2 = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high2 = int(row[5])
            low2 = int(row[6])
        except ValueError:
            print(f"Missing data for {current_date2}, filename2")
        else:
            dates.append(current_date2)
            highs.append(high2)
            lows.append(low2)

'''Plot high and low temperatures'''
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='black', alpha=0.1)

title = "Comparison Sitka and Death Valley"
'''Format plot'''
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
