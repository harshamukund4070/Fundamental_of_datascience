# Question:
# 12. Scenario: Analyze monthly temperature and rainfall data for a city.
# 1. Develop a Python program to create a line plot of the monthly temperature data.
# 2. Develop a Python program to create a scatter plot of the monthly rainfall data.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-12_temperature_rainfall.csv")

# Line plot of temperature
plt.plot(data["month"], data["temperature"], marker="o")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.title("Monthly Temperature")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Scatter plot of rainfall
plt.scatter(data["month"], data["rainfall"])
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.title("Monthly Rainfall")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
