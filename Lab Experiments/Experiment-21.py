import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("data21.csv")

print("Mean:\n", df[["age", "fat"]].mean())
print("\nMedian:\n", df[["age", "fat"]].median())
print("\nStandard Deviation:\n", df[["age", "fat"]].std())

# Boxplots
df[["age", "fat"]].plot(kind="box", figsize=(7,5))
plt.title("Boxplots of Age and % Fat")
plt.ylabel("Value")
plt.grid(axis="y", alpha=0.3)
plt.show()

# Scatter plot
plt.figure(figsize=(7,5))
plt.scatter(df["age"], df["fat"])
plt.xlabel("Age")
plt.ylabel("% Fat")
plt.title("Age vs % Body Fat")
plt.grid(alpha=0.3)
plt.show()

# Q-Q plots
fig, axes = plt.subplots(1, 2, figsize=(10,4))
stats.probplot(df["age"], dist="norm", plot=axes[0])
axes[0].set_title("Q-Q Plot - Age")
stats.probplot(df["fat"], dist="norm", plot=axes[1])
axes[1].set_title("Q-Q Plot - % Fat")
plt.tight_layout()
plt.show()
