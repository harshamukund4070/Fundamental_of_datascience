# Question:
# 11. Scenario: You are a data scientist working for a company that sells products online.
# Create a simple plot to show the sales of a product over time.
# 1. Write code to create a simple line plot in Python using Matplotlib to predict sales
#    happened in a month.
# 2. Write code to create a scatter plot in Python using Matplotlib to predict sales
#    happened in a month.
# 3. Develop a Python program to create a bar plot of the monthly sales data.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Exp-11_monthly_sales.csv")
months = data["month"]
sales = data["sales"]

# Simple linear prediction for the next month
x = np.arange(len(sales))
slope, intercept = np.polyfit(x, sales, 1)
next_month_prediction = slope * len(sales) + intercept
print(f"Predicted sales for next month: {next_month_prediction:.2f}")

# Line plot
plt.plot(months, sales, marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Line Plot")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Scatter plot
plt.scatter(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Scatter Plot")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# Bar plot
plt.bar(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Bar Plot")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
