# Question:
# Scenario: Create basic Matplotlib plots using monthly company sales data.
# 1. Develop a Python program to create a line plot of monthly sales data.
# 2. Develop a Python program to create a bar plot of monthly sales data.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("Exp-10_monthly_sales.csv")

months = sales_data["month"]
sales = sales_data["sales"]

# Line plot
plt.plot(months, sales, marker="o")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales - Line Plot")
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
