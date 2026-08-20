# Question:
# Use KNN to predict whether a patient has a medical condition (1) or not (0).
# Allow the user to enter symptom features and k (number of neighbors).
# Input: Exp-30_patient_symptoms.csv

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

d=pd.read_csv("Exp-30_patient_symptoms.csv")
features=["fever","cough","fatigue","pain"]
k=int(input("Enter k: "))
if k<1 or k>len(d): raise ValueError("Invalid k.")
model=Pipeline([("scale",StandardScaler()),("knn",KNeighborsClassifier(n_neighbors=k))])
model.fit(d[features],d.condition)
v=[float(input(f"{f} (0-10): ")) for f in features]
p=model.predict(np.array([v]))[0]
print("Prediction:",1 if p==1 else 0)
d.groupby("condition")[features].mean().T.plot(kind="bar")
plt.xlabel("Symptom"); plt.ylabel("Average Level"); plt.title("Symptoms by Condition")
plt.tight_layout(); plt.show()
