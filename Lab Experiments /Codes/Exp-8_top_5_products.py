# Question:
# Scenario: Analyze monthly sales data stored in a Pandas DataFrame.
# Find the top 5 products that have been sold the most in the past month.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv("Exp-8_sales_data.csv")

top_5 = (sales_data.groupby("product_name")["quantity_sold"]
         .sum()
         .sort_values(ascending=False)
         .head(5))

print("Top 5 products sold:")
print(top_5)

top_5.plot(kind="bar")
plt.xlabel("Product")
plt.ylabel("Total Quantity Sold")
plt.title("Top 5 Best-Selling Products")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
