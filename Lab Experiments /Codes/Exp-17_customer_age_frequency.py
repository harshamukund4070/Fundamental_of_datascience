# Question:
# 17. Scenario: Analyze monthly sales data stored in a Pandas DataFrame.
# Develop Python code to find the frequency distribution of the ages
# of customers who made a purchase in the past month.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-17_customer_sales.csv")

age_frequency = data["age"].value_counts().sort_index()

print("Frequency distribution of customer ages:")
print(age_frequency)

plt.bar(age_frequency.index.astype(str), age_frequency.values)
plt.xlabel("Customer Age")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Customer Ages")
plt.tight_layout()
plt.show()
