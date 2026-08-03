import numpy as np
training = np.array([5,8,10,12,15,18,20,22,25,28])
projects = np.array([2,3,4,5,6,7,8,9,10,11])
rating = np.array([60,65,70,74,79,84,88,91,95,98])
print("Mean:", np.mean(rating))
print("Variance:", np.var(rating, ddof=1))
print("Standard Deviation:", np.std(rating, ddof=1))
print("Covariance (Training, Rating):", np.cov(training, rating)[0,1])
print("Covariance (Projects, Rating):", np.cov(projects, rating)[0,1])
corr_training = np.corrcoef(training, rating)[0,1]
corr_projects = np.corrcoef(projects, rating)[0,1]
print("Correlation (Training, Rating):", corr_training)
print("Correlation (Projects, Rating):", corr_projects)
if abs(corr_training) > abs(corr_projects):
    print("Training Hours have stronger impact.")
else:
    print("Projects Completed have stronger impact.")
print("\nHR Policies:")
print("- Employee training")
print("- Performance incentives")
print("- Skill development")
print("- Career growth opportunities")