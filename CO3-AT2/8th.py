import numpy as np

scores = np.array([72,75,68,80,77,73,79,81,76,74,78,69,70,82,71,75,77,73,80,76,74,79,72,81,78])

mean = np.mean(scores)
std = np.std(scores, ddof=1)
se = std / np.sqrt(len(scores))

print("Mean:", mean)
print("Standard Deviation:", std)
print("Standard Error:", se)

print("\nComparison:")
print("Standard Deviation measures data spread.")
print("Standard Error measures accuracy of the sample mean.")