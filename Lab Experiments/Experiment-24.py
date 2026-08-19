import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("rare_elements.csv")
data = df.iloc[:, 0].dropna().to_numpy()

sample_size = int(input(f"Enter sample size (1-{len(data)}): "))
confidence_level = float(input("Enter confidence level (e.g. 0.95): "))
precision = float(input("Enter desired level of precision (margin of error): "))

if sample_size < 2 or sample_size > len(data):
    raise ValueError("Invalid sample size.")
if not 0 < confidence_level < 1:
    raise ValueError("Confidence level must be between 0 and 1.")

sample = data[:sample_size]
mean = np.mean(sample)
std = np.std(sample, ddof=1)
alpha = 1 - confidence_level
t_critical = stats.t.ppf(1 - alpha/2, sample_size - 1)
margin = t_critical * std / np.sqrt(sample_size)
ci = (mean - margin, mean + margin)

print(f"\nPoint estimate (sample mean) = {mean:.4f}")
print(f"{confidence_level*100:.1f}% CI = ({ci[0]:.4f}, {ci[1]:.4f})")
print(f"Calculated margin of error = {margin:.4f}")
print(f"Desired precision = {precision:.4f}")
print("Precision requirement met." if margin <= precision else
      "Precision requirement not met; use a larger sample.")

plt.hist(sample, bins=8, edgecolor="black")
plt.axvline(mean, linestyle="--", label=f"Mean = {mean:.2f}")
plt.xlabel("Concentration")
plt.ylabel("Frequency")
plt.title("Rare Element Concentration")
plt.legend()
plt.show()
