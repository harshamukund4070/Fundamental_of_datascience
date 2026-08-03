import math
from scipy.stats import norm

mean = 4.8
std = 1.5
n = 100

z = norm.ppf(0.975)
margin = z * std / math.sqrt(n)

lower = mean - margin
upper = mean + margin

print("Estimated Population Mean =", mean)
print("95% Confidence Interval =", (lower, upper))

print("\nFrequentist Interpretation:")
print("95% of similarly constructed confidence intervals")
print("would contain the true population mean.")