import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("fuel_efficiency.csv")
fuel=data["FuelEfficiency"].to_numpy()
average=np.mean(fuel)
improvement=((fuel[-1]-fuel[0])/fuel[0])*100
print(average)
print(improvement)
plt.figure(figsize=(6,4))
plt.bar(data["CarModel"],fuel)
plt.title("Fuel Efficiency")
plt.xlabel("Car Model")
plt.ylabel("MPG")
plt.show()
plt.figure(figsize=(6,4))
plt.plot(data["CarModel"],fuel,marker="o")
plt.title("Fuel Efficiency")
plt.xlabel("Car Model")
plt.ylabel("MPG")
plt.grid(True)
plt.show()