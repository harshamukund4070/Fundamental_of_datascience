# Question:
# Read rare_elements.csv and allow the user to input sample size, confidence
# level and desired precision. Perform point estimation and calculate a
# confidence interval for the population mean.
# Input: Exp-24_rare_elements.csv

import numpy as np
from scipy import stats

x=np.loadtxt("Exp-24_rare_elements.csv",delimiter=",",skiprows=1)
n=int(input("Enter sample size: ")); conf=float(input("Enter confidence level (%): "))/100
precision=float(input("Enter desired precision (maximum margin of error): "))
if n<2 or n>len(x): raise ValueError("Invalid sample size.")
s=x[:n]; mean=s.mean(); sd=s.std(ddof=1)
crit=stats.t.ppf((1+conf)/2,n-1); margin=crit*sd/np.sqrt(n)
print("Point estimate:",mean)
print("Confidence interval:",(mean-margin,mean+margin))
print("Margin of error:",margin)
z=stats.norm.ppf((1+conf)/2)
print("Approximate sample size for requested precision:",int(np.ceil((z*sd/precision)**2)))
