# Question:
# Use Pandas to calculate a confidence interval estimating the true population
# mean customer rating from customer_reviews.csv.
# Input: Exp-25_customer_reviews.csv

import pandas as pd
from scipy import stats

d=pd.read_csv("Exp-25_customer_reviews.csv"); x=d.rating.dropna()
conf=float(input("Enter confidence level (%): "))/100
m=x.mean(); margin=stats.t.ppf((1+conf)/2,len(x)-1)*stats.sem(x)
print("Average rating:",m)
print("Confidence interval:",(m-margin,m+margin))
print("Customer satisfaction (rating >= 4):",round((x>=4).mean()*100,2),"%")
