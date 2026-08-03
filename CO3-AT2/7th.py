import numpy as np

ratings = np.array([4,5,3,4,5,4,3,5,4,4,5,3,4,5,4,3,5,4,5,4])

mean = np.mean(ratings)
variance = np.var(ratings, ddof=1)
standard_error = np.std(ratings, ddof=1) / np.sqrt(len(ratings))

print("Sample Mean:", mean)
print("Sample Variance:", variance)
print("Standard Error:", standard_error)

print("\nStandard Error indicates how accurately")
print("the sample mean estimates the population mean.")