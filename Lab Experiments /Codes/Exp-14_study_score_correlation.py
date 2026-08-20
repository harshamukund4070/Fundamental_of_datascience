# Question:
# 14. Scenario: Explore the correlation between students' study time and exam scores.
# Identify potential correlation and use plotting functions to visualize the relationship.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("Exp-14_study_scores.csv")

correlation = data["study_hours"].corr(data["exam_score"])
print(f"Correlation between study time and exam score: {correlation:.3f}")

if correlation > 0:
    print("There is a positive correlation: higher study time tends to be associated with higher scores.")
elif correlation < 0:
    print("There is a negative correlation: higher study time tends to be associated with lower scores.")
else:
    print("There is little or no linear correlation.")

plt.scatter(data["study_hours"], data["exam_score"])
plt.xlabel("Study Time (hours)")
plt.ylabel("Exam Score")
plt.title("Study Time vs Exam Score")

# Trend line
x = data["study_hours"]
y = data["exam_score"]
slope, intercept = np.polyfit(x, y, 1)
plt.plot(x, slope * x + intercept)

plt.tight_layout()
plt.show()
