# Question:
# Scenario: Analyze sales data for the past month.
# Find the average price of all products sold in the past month.
# Assume a 3x3 matrix with each row representing sales for a different product.
# The program must take CSV input.

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Exp-2_sales_prices.csv", delimiter=",", skiprows=1)
prices = data[:, 0]

average_price = np.mean(prices)

print(f"Average price of all products sold: {average_price:.2f}")

plt.hist(prices, bins=5, edgecolor="black")
plt.xlabel("Product Price")
plt.ylabel("Number of Products")
plt.title("Distribution of Product Prices")
plt.tight_layout()
plt.show()
