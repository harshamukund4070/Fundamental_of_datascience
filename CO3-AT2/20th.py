import math
from scipy.stats import t

mean_diff = 200
std_diff = 350
n = 50

t_stat = mean_diff / (std_diff / math.sqrt(n))
df = n - 1

p_value = 2 * (1 - t.cdf(abs(t_stat), df))

print("Paired t Statistic =", t_stat)
print("p-value =", p_value)

if p_value < 0.05:
    print("Reject H0")
    print("Model B significantly outperforms Model A.")
else:
    print("Fail to Reject H0")
    print("No significant difference.")

print("\nInterpretation:")
print("A significant result indicates the lower MAE")
print("of Model B is unlikely due to random variation.")