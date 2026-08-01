import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("sales_data.csv")
sales=data["Sales"].to_numpy()
total=np.sum(sales)
increase=((sales[-1]-sales[0])/sales[0])*100
print(total)
print(increase)
plt.figure(figsize=(6,4))
plt.plot(data["Quarter"],sales,marker="o")
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
plt.figure(figsize=(6,4))
plt.bar(data["Quarter"],sales)
plt.title("Quarterly Sales")
plt.xlabel("Quarter")
plt.ylabel("Sales")
plt.show()