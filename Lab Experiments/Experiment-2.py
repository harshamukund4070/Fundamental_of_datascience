import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("product_sales.csv")
sales=data.to_numpy()
avg=np.mean(sales)
print(avg)
plt.figure(figsize=(6,4))
plt.hist(sales.flatten(),bins=5)
plt.title("Distribution of Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()