# Question:
# 15. Scenario: Analyze daily temperature readings for different cities over a year.
# 1. Calculate the mean temperature for each city.
# 2. Calculate the standard deviation of temperature for each city.
# 3. Determine the city with the highest temperature range.
# 4. Find the city with the most consistent temperature (lowest standard deviation).
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-15_city_temperatures.csv")

cities = data.columns

means = data[cities].mean()
std_devs = data[cities].std()
ranges = data[cities].max() - data[cities].min()

print("Mean temperature for each city:")
print(means)

print("\nStandard deviation for each city:")
print(std_devs)

highest_range_city = ranges.idxmax()
consistent_city = std_devs.idxmin()

print(f"\nCity with highest temperature range: {highest_range_city}")
print(f"Highest temperature range: {ranges[highest_range_city]:.2f} °C")

print(f"\nMost consistent city: {consistent_city}")
print(f"Lowest standard deviation: {std_devs[consistent_city]:.2f} °C")

plt.bar(cities, means)
plt.xlabel("City")
plt.ylabel("Mean Temperature (°C)")
plt.title("Mean Temperature by City")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
