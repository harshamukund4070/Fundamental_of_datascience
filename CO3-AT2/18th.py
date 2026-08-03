from scipy.stats import ttest_ind_from_stats

mean1 = 18
std1 = 5
n1 = 400

mean2 = 20
std2 = 6
n2 = 420

t_stat, p_value = ttest_ind_from_stats(
    mean1, std1, n1,
    mean2, std2, n2
)

print("t Statistic =", t_stat)
print("p-value =", p_value)

if p_value < 0.05:
    print("Reject H0")
    print("Feature B significantly increases engagement.")
else:
    print("Fail to Reject H0")