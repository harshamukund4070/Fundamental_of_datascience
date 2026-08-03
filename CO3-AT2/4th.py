import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
traffic = [12000,13500,14500,16000,17500,19000,21000,22500,24000,26000]
rain = [0,5,10,15,20,25,30,35,40,45]
speed = [55,50,48,45,42,38,35,32,28,25]
accidents = [2,3,4,5,6,8,10,12,14,16]
df = pd.DataFrame({
    "Traffic": traffic,
    "Rainfall": rain,
    "Speed": speed,
    "Accidents": accidents
})
print(df.describe())
print("\nCovariance Matrix")
print(df.cov())
print("\nCorrelation Matrix")
print(df.corr())
print("\nCorrelation with Accidents")
print(df.corr()["Accidents"])
plt.scatter(traffic, accidents)
plt.xlabel("Traffic Volume")
plt.ylabel("Accidents")
plt.title("Traffic vs Accidents")
plt.show()
plt.scatter(rain, accidents)
plt.xlabel("Rainfall")
plt.ylabel("Accidents")
plt.title("Rainfall vs Accidents")
plt.show()
plt.scatter(speed, accidents)
plt.xlabel("Average Speed")
plt.ylabel("Accidents")
plt.title("Speed vs Accidents")
plt.show()
print("\nRecommendations:")
print("- Reduce speed limits")
print("- Improve drainage")
print("- Install traffic monitoring")
print("- Increase road safety awareness")