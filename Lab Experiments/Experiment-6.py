import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv("grocery_data.csv")
discount=10
tax=5
subtotal=(data["Price"]*data["Quantity"]).sum()
discount_amount=subtotal*discount/100
taxable=subtotal-discount_amount
tax_amount=taxable*tax/100
total=taxable+tax_amount
print(total)
plt.figure(figsize=(6,4))
plt.bar(data["Item"],data["Price"]*data["Quantity"])
plt.title("Item Cost")
plt.xlabel("Item")
plt.ylabel("Cost")
plt.show()
plt.figure(figsize=(6,4))
plt.pie(data["Price"]*data["Quantity"],labels=data["Item"],autopct="%1.1f%%")
plt.title("Purchase Distribution")
plt.show()