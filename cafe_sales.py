import numpy as np

units = np.array([
    [30, 20, 10],
    [25, 30, 15],
    [40, 25, 20],
    [35, 15, 25]
])

price = np.array([100, 150, 200])

revenue = units * price

revenue_per_day = revenue.sum(axis=1)
units_per_item = units.sum(axis=0)
best_day = revenue_per_day.argmax()
coffee_last_two_days = units[2:, 1]

print("Revenue per day:", revenue_per_day)
print("Units sold per item:", units_per_item)
print("Best day index:", best_day)
print("Coffee, last two days:", coffee_last_two_days)