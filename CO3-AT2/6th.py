import numpy as np

spending = np.array([120,145,130,155,160,125,140,135,150,170,165,155])

print("Average Spending:", np.mean(spending))
print("Standard Deviation:", np.std(spending, ddof=1))

print("\nThese values are point estimates because they estimate")
print("the population mean and population standard deviation.")