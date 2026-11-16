
import numpy as np

np.random.seed(7)

readings = np.random.randint(20, 41, size=(6, 3))

print(readings)

mean_values = readings.mean(axis=0)
print("Mean per sensor:", mean_values)

std_values = readings.std(axis=0)
normalized = (readings - mean_values) / std_values

print("Normalized column means:", normalized.mean(axis=0))

peak_hours = readings.argmax(axis=0)
print("Hour of max per sensor:", peak_hours)

summary = np.vstack([readings, mean_values])
print(summary.shape)

np.random.seed(7)
readings_again = np.random.randint(20, 41, size=(6, 3))

print("Reproducible:", np.array_equal(readings, readings_again))
