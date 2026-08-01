import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("monthly_sales.csv")
top=data.groupby("Product")["Quantity"].sum().sort_values(ascending=False).head(5)
print(top)
top.plot(kind="bar")
plt.title("Top 5 Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.show()
top.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Top 5 Product Share")
plt.show()