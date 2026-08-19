import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("data22.csv")

for group in ["Drug", "Placebo"]:
    x = df.loc[df["group"] == group, "reduction"]
    n = len(x)
    mean = x.mean()
    sem = stats.sem(x)
    ci = stats.t.interval(0.95, df=n-1, loc=mean, scale=sem)
    print(f"{group} group:")
    print(f"Mean reduction = {mean:.2f}")
    print(f"95% CI = ({ci[0]:.2f}, {ci[1]:.2f})\n")

# Graph
df.boxplot(column="reduction", by="group")
plt.title("Blood Pressure Reduction by Group")
plt.suptitle("")
plt.xlabel("Group")
plt.ylabel("Reduction")
plt.show()
