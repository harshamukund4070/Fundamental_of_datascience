import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv("customer_reviews.csv")
ratings = df["rating"].dropna()

mean_rating = ratings.mean()
sem = stats.sem(ratings)
ci = stats.t.interval(0.95, df=len(ratings)-1, loc=mean_rating, scale=sem)

print("Average rating:", round(mean_rating, 3))
print("95% Confidence Interval for population mean:")
print(f"({ci[0]:.3f}, {ci[1]:.3f})")

# Simple satisfaction measure: ratings >= 4 are satisfied
satisfaction = (ratings >= 4).mean() * 100
print(f"Customer satisfaction (rating >= 4): {satisfaction:.2f}%")

plt.hist(ratings, bins=[1,2,3,4,5,6], align="left", rwidth=0.8)
plt.xlabel("Rating")
plt.ylabel("Number of Reviews")
plt.title("Customer Rating Distribution")
plt.xticks([1,2,3,4,5])
plt.show()
