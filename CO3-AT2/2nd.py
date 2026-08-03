import numpy as np
visits = np.array([5,8,10,12,15,18,20,23,25,28])
time = np.array([20,25,30,35,40,45,50,55,60,70])
purchase = np.array([1200,1800,2500,3200,4000,5000,6200,7300,8500,10000])
print("Mean:", np.mean(purchase))
print("Variance:", np.var(purchase, ddof=1))
print("Standard Deviation:", np.std(purchase, ddof=1))
print("Covariance (Visits, Purchase):", np.cov(visits, purchase)[0,1])
print("Covariance (Time, Purchase):", np.cov(time, purchase)[0,1])
corr_visits = np.corrcoef(visits, purchase)[0,1]
corr_time = np.corrcoef(time, purchase)[0,1]
print("Correlation (Visits, Purchase):", corr_visits)
print("Correlation (Time, Purchase):", corr_time)
if abs(corr_visits) > abs(corr_time):
    print("Website Visits better predict spending.")
else:
    print("Time Spent better predicts spending.")
print("\nMarketing Strategies:")
print("- Personalized recommendations")
print("- Loyalty rewards")
print("- Improve website engagement")
print("- Target high-value customers")