import numpy as np

delivery = np.array([22,25,18,30,27,24,21,19,26,23,28,20,24,25,22])

print("Point Estimate of Mean:", np.mean(delivery))
print("Point Estimate of Variance:", np.var(delivery, ddof=1))

print("\nInterpretation:")
print("The sample mean estimates the population mean.")
print("The sample variance estimates the population variance.")