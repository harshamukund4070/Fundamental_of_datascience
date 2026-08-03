import numpy as np
from scipy.stats import t

mean = 498
std = 12
n = 50

t_value = t.ppf(0.975, n-1)
margin = t_value * (std / np.sqrt(n))

lower = mean - margin
upper = mean + margin

print("95% Confidence Interval:")
print((lower, upper))

if lower <= 500 <= upper:
    print("Target weight of 500 g is plausible.")
else:
    print("Target weight of 500 g is not plausible.")