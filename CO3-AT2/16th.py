prevalence = 0.02
sensitivity = 0.95
specificity = 0.90

false_positive = 1 - specificity

positive = (sensitivity * prevalence) + \
           (false_positive * (1 - prevalence))

posterior = (sensitivity * prevalence) / positive

print("Posterior Probability =", posterior)

print("\nExplanation:")
print("Even with high sensitivity,")
print("low disease prevalence causes many false positives.")