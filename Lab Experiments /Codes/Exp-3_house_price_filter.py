# Question:
# Scenario: Analyze a neighborhood house dataset stored in a CSV file.
# Each row represents a house and columns contain features such as bedrooms,
# square footage, and sale price.
# Using NumPy arrays, find the average sale price of houses with more than
# four bedrooms.
# The program must take CSV input.

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Exp-3_house_data.csv", delimiter=",", skiprows=1)
bedrooms = data[:, 0]
sale_price = data[:, 2]

filtered_prices = sale_price[bedrooms > 4]

if len(filtered_prices) > 0:
    average_price = np.mean(filtered_prices)
    print(f"Average sale price of houses with more than 4 bedrooms: {average_price:.2f}")
else:
    print("No houses have more than 4 bedrooms.")

plt.scatter(bedrooms, sale_price)
plt.xlabel("Number of Bedrooms")
plt.ylabel("Sale Price")
plt.title("Bedrooms vs Sale Price")
plt.tight_layout()
plt.show()
