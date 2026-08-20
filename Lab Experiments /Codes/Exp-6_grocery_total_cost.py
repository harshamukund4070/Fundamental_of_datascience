# Question:
# Scenario: Calculate the total cost of a customer's grocery purchase.
# Item prices and quantities are given separately. Calculate the total cost
# including the applicable discount and tax rates.
# The program must take CSV input.

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Exp-6_grocery_items.csv", delimiter=",", skiprows=1)
prices = data[:, 0]
quantities = data[:, 1]

discount_rate = float(input("Enter discount rate (%): "))
tax_rate = float(input("Enter tax rate (%): "))

subtotal = np.sum(prices * quantities)
discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
tax = after_discount * tax_rate / 100
total_cost = after_discount + tax

print(f"Subtotal: {subtotal:.2f}")
print(f"Discount: {discount:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total cost: {total_cost:.2f}")

item_totals = prices * quantities
plt.bar(range(1, len(item_totals) + 1), item_totals)
plt.xlabel("Item Number")
plt.ylabel("Item Cost")
plt.title("Cost of Each Grocery Item")
plt.tight_layout()
plt.show()
