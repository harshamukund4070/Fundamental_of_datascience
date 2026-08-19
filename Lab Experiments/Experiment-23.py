import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("data23.csv")

a = df.loc[df["design"] == "A", "converted"]
b = df.loc[df["design"] == "B", "converted"]

# Welch's two-sample t-test on 0/1 conversion observations
t_stat, p_value = stats.ttest_ind(a, b, equal_var=False)

print("Mean conversion rate - Design A:", a.mean())
print("Mean conversion rate - Design B:", b.mean())
print("t-statistic:", t_stat)
print("p-value:", p_value)

alpha = 0.05
if p_value < alpha:
    print("Conclusion: Statistically significant difference.")
else:
    print("Conclusion: No statistically significant difference.")

plt.bar(["Design A", "Design B"], [a.mean(), b.mean()])
plt.ylabel("Mean Conversion Rate")
plt.title("A/B Test Conversion Rates")
plt.ylim(0, max(a.mean(), b.mean()) * 1.3)
plt.show()
