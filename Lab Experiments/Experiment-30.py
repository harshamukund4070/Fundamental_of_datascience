import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("patients.csv")
features = ["fever", "cough", "fatigue", "headache"]
X = df[features]
y = df["condition"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

k = int(input("Enter k (number of neighbors): "))

if k <= 0 or k > len(X_train):
    raise ValueError("k must be between 1 and the training sample size.")

model = KNeighborsClassifier(n_neighbors=k)
model.fit(X_train_scaled, y_train)

print("Test accuracy:", round(accuracy_score(y_test, model.predict(X_test_scaled)), 4))

print("\nEnter patient symptoms (0 = No, 1 = Yes):")
values = [int(input(f"{f}: ")) for f in features]

new_patient = scaler.transform([values])
prediction = model.predict(new_patient)[0]

print("Predicted condition:", "Condition present (1)" if prediction == 1
      else "No condition (0)")

# Graph: test-set prediction distribution
pred_test = model.predict(X_test_scaled)
pd.Series(pred_test).value_counts().sort_index().plot(
    kind="bar", figsize=(6,4)
)
plt.xlabel("Predicted Class")
plt.ylabel("Number of Patients")
plt.title("KNN Predicted Class Distribution")
plt.xticks([0,1], ["No Condition", "Condition"], rotation=0)
plt.show()
