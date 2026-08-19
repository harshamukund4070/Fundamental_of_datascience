import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("data26.csv")
control = df.loc[df["group"] == "Control", "response"]
treatment = df.loc[df["group"] == "Treatment", "response"]

t_stat, p_value = stats.ttest_ind(treatment, control, equal_var=False)

print("Control mean:", control.mean())
print("Treatment mean:", treatment.mean())
print("t-statistic:", t_stat)
print("p-value:", p_value)

alpha = 0.05
print("Result:", "Significant treatment effect" if p_value < alpha
      else "No statistically significant treatment effect")

# Visualize means and p-value
plt.figure(figsize=(7,5))
bars = plt.bar(["Control", "Treatment"], [control.mean(), treatment.mean()])
plt.ylabel("Mean Response")
plt.title(f"Treatment Effect (p-value = {p_value:.4g})")
plt.grid(axis="y", alpha=0.3)
plt.show()
