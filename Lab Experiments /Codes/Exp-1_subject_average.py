# Question:
# Scenario: Analyze student performance data for a class of students.
# Calculate the average score for each subject and identify the subject with
# the highest average score. Subjects: Math, Science, English, History.
# Assume a 4x4 matrix stores marks of each student in the given order.
# The program must take CSV input.

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("Exp-1_student_scores.csv", delimiter=",", skiprows=1)
subjects = ["Math", "Science", "English", "History"]

averages = np.mean(data, axis=0)
highest_index = np.argmax(averages)

print("Average score for each subject:")
for subject, avg in zip(subjects, averages):
    print(f"{subject}: {avg:.2f}")

print("Subject with highest average:", subjects[highest_index])

plt.bar(subjects, averages)
plt.xlabel("Subjects")
plt.ylabel("Average Score")
plt.title("Average Student Score by Subject")
plt.tight_layout()
plt.show()
