# Question:
# Scenario: Analyze an e-commerce Pandas DataFrame named order_data.
# Find:
# 1. The total number of orders made by each customer.
# 2. The average order quantity for each product.
# 3. The earliest and latest order dates in the dataset.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

order_data = pd.read_csv("Exp-7_order_data.csv")
order_data["order_date"] = pd.to_datetime(order_data["order_date"])

orders_by_customer = order_data.groupby("customer_id").size()
avg_quantity_by_product = order_data.groupby("product_name")["order_quantity"].mean()
earliest_date = order_data["order_date"].min()
latest_date = order_data["order_date"].max()

print("\nTotal number of orders by each customer:")
print(orders_by_customer)

print("\nAverage order quantity for each product:")
print(avg_quantity_by_product)

print("\nEarliest order date:", earliest_date.date())
print("Latest order date:", latest_date.date())

orders_by_customer.plot(kind="bar")
plt.xlabel("Customer ID")
plt.ylabel("Number of Orders")
plt.title("Orders by Customer")
plt.tight_layout()
plt.show()
