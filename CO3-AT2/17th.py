from statsmodels.stats.proportion import proportions_ztest

success = [250, 312]
total = [5000, 5200]

rateA = success[0] / total[0]
rateB = success[1] / total[1]

print("Conversion Rate A =", rateA)
print("Conversion Rate B =", rateB)

print("\nH0: pA = pB")
print("H1: pB > pA")

z_stat, p_value = proportions_ztest(success, total)

print("Z Statistic =", z_stat)
print("p-value =", p_value)

if p_value < 0.05:
    print("Reject H0")
    print("Page B performs better.")
else:
    print("Fail to Reject H0")