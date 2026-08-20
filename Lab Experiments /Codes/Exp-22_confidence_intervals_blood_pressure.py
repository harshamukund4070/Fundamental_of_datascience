# Question:
# Calculate the 95% confidence interval for mean blood-pressure reduction
# for the new-drug group and the placebo group.
# Input: Exp-22_blood_pressure.csv

import pandas as pd
from scipy import stats

d=pd.read_csv("Exp-22_blood_pressure.csv")
for g in ["Drug","Placebo"]:
    x=d.loc[d.group==g,"reduction"]
    m=x.mean(); margin=stats.t.ppf(.975,len(x)-1)*stats.sem(x)
    print(g, "mean =",round(m,2), "95% CI = (",round(m-margin,2),",",round(m+margin,2),")")
