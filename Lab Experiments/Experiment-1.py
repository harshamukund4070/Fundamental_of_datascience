import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("student_scores.csv")
student_scores=data.to_numpy()
subjects=["Math","Science","English","History"]
avg=np.mean(student_scores,axis=0)
highest=subjects[np.argmax(avg)]
print(avg)
print(highest)
plt.figure(figsize=(6,4))
plt.bar(subjects,avg)
plt.title("Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average")
plt.grid(axis="y")
plt.show()
plt.figure(figsize=(6,4))
plt.plot(subjects,avg,marker="o")
plt.title("Average Subject Scores")
plt.xlabel("Subjects")
plt.ylabel("Average")
plt.grid(True)
plt.show()