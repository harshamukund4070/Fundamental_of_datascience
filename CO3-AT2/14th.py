import math
from scipy.stats import norm

n = 500
defective = 22

p = defective / n

z = norm.ppf(0.975)
margin = z * math.sqrt((p * (1 - p)) / n)

lower = p - margin
upper = p + margin

print("Estimated Defect Rate =", p)
print("95% Confidence Interval =", (lower, upper))

print("\nInterpretation:")
print("The interval estimates the true defect rate with 95% confidence.")