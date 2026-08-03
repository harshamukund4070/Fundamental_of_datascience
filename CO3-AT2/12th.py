import numpy as np
from scipy.stats import ttest_ind

before = np.array([50,52,49,55,53,51,54,50])
after = np.array([58,60,57,62,59,61,63,58])

t_stat, p_value = ttest_ind(after, before)

print("t Statistic =", t_stat)
print("p-value =", p_value)

if p_value < 0.05:
    print("Reject H0")
    print("Campaign significantly increased sales.")
else:
    print("Fail to Reject H0")
    print("No significant improvement.")

print("Interpretation:")
print("Small p-value means strong evidence against H0.")