# Question:
# Scenario: Analyze company sales performance over four quarters.
# Calculate the total sales for the year and determine the percentage increase
# in sales from the first quarter to the fourth quarter.
# The program must take CSV input.

import numpy as np
import matplotlib.pyplot as plt

sales_data = np.loadtxt("Exp-4_quarterly_sales.csv", delimiter=",", skiprows=1)

total_sales = np.sum(sales_data)
percentage_increase = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100

print(f"Total sales for the year: {total_sales:.2f}")
print(f"Percentage increase from Q1 to Q4: {percentage_increase:.2f}%")

quarters = ["Q1", "Q2", "Q3", "Q4"]
plt.plot(quarters, sales_data, marker="o")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.title("Quarterly Sales Performance")
plt.tight_layout()
plt.show()
