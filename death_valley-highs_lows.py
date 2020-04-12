import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get high temperatures  from this file.
    dates,highs, lows = [], [], []
    for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            try:
                high = int(row[4])
                low = int(row[5])
            except  ValueError:
                print(f"Missing date for {current_date}")
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

    # plot the high tempetures
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
ax.set_title("Death Valley CA Daily high and low temperatures, 2018", fontsize=24)
ax.set_xlabel('', fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)


plt.show()