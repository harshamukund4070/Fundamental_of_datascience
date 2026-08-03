import math
from scipy.stats import t

# Given data
mu = 10
x_bar = 9.5
s = 1.8
n = 36
alpha = 0.05

# Hypotheses
print("H0: μ = 10")
print("H1: μ ≠ 10")

# Test Statistic
t_stat = (x_bar - mu) / (s / math.sqrt(n))
df = n - 1

# p-value
p_value = 2 * (1 - t.cdf(abs(t_stat), df))

print("t Statistic =", t_stat)
print("p-value =", p_value)

if p_value < alpha:
    print("Reject H0")
    print("Average battery life is significantly different from 10 hours.")
else:
    print("Fail to Reject H0")
    print("No significant difference from 10 hours.")   