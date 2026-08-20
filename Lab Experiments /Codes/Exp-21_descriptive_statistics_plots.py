# Question:
# Calculate mean, median and standard deviation of age and %fat using Pandas.
# Draw boxplots for age and %fat, a scatter plot, and Q-Q plots.
# Input: Exp-21_age_bodyfat.csv

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

d=pd.read_csv("Exp-21_age_bodyfat.csv")
for c in ["age","fat_percent"]:
    print(c, "Mean:",d[c].mean(),"Median:",d[c].median(),"SD:",d[c].std())
d[["age","fat_percent"]].boxplot()
plt.title("Age and Body Fat Boxplots"); plt.tight_layout(); plt.show()
plt.scatter(d.age,d.fat_percent)
plt.xlabel("Age"); plt.ylabel("Body Fat (%)"); plt.title("Age vs Body Fat"); plt.show()
fig,ax=plt.subplots(1,2,figsize=(10,4))
stats.probplot(d.age,dist="norm",plot=ax[0]); ax[0].set_title("Q-Q Plot: Age")
stats.probplot(d.fat_percent,dist="norm",plot=ax[1]); ax[1].set_title("Q-Q Plot: Body Fat")
plt.tight_layout(); plt.show()
