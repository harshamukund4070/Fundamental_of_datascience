# Question:
# Determine whether there is a statistically significant difference in mean
# conversion rates between website designs A and B.
# Input: Exp-23_ab_conversion.csv

import pandas as pd
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

d=pd.read_csv("Exp-23_ab_conversion.csv")
a=d.loc[d.design=="A","conversion_rate"]; b=d.loc[d.design=="B","conversion_rate"]
t,p=ttest_ind(a,b,equal_var=False)
print("Mean A:",a.mean(),"Mean B:",b.mean(),"t-statistic:",t,"p-value:",p)
print("Statistically significant." if p<.05 else "Not statistically significant.")
plt.boxplot([a,b],labels=["Design A","Design B"]); plt.ylabel("Conversion Rate")
plt.title("A/B Test"); plt.show()
