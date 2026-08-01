import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("house_data.csv")
house_data=data.to_numpy()
filtered=house_data[house_data[:,0]>4]
avg_price=np.mean(filtered[:,2])
print(avg_price)
plt.figure(figsize=(6,4))
plt.scatter(data["Bedrooms"],data["SalePrice"])
plt.title("Bedrooms vs Sale Price")
plt.xlabel("Bedrooms")
plt.ylabel("Sale Price")
plt.grid(True)
plt.show()
