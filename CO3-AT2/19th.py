from statsmodels.stats.proportion import proportions_ztest

success = [4800, 5300]
total = [100000, 100000]

rate_old = success[0] / total[0]
rate_new = success[1] / total[1]

print("Old CTR =", rate_old)
print("New CTR =", rate_new)

z_stat, p_value = proportions_ztest(success, total)

print("Z Statistic =", z_stat)
print("p-value =", p_value)

if p_value < 0.05:
    print("Statistically Significant Improvement")
else:
    print("No Significant Improvement")

print("\nPractical Significance:")
print("Statistical significance does not always")
print("mean the improvement is large enough")
print("to matter in business.")