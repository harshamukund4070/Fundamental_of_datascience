# Question:
# Compare a control/placebo group with a treatment group using hypothesis testing.
# Calculate the p-value and use Matplotlib to visualize the data and p-value.
# Input: Exp-26_treatment_data.csv

import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

d=pd.read_csv("Exp-26_treatment_data.csv")
c=d.loc[d.group=="Control","outcome"]; t=d.loc[d.group=="Treatment","outcome"]
stat,p=ttest_ind(t,c,equal_var=False)
print("Control mean:",c.mean(),"Treatment mean:",t.mean())
print("t-statistic:",stat,"p-value:",p)
print("Reject H0: significant effect." if p<.05 else "Fail to reject H0.")
plt.boxplot([c,t],labels=["Control","Treatment"]); plt.ylabel("Outcome")
plt.title("Treatment vs Control"); plt.show()
plt.bar(["p-value","alpha"],[p,.05]); plt.ylabel("Value"); plt.title("p-value vs 0.05"); plt.show()
