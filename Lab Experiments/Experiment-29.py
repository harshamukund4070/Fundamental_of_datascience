import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score

df = pd.read_csv("iris.csv")
X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(max_depth=4, random_state=42)
model.fit(X_train, y_train)

print("Test accuracy:", round(accuracy_score(y_test, model.predict(X_test)), 4))

sl = float(input("Sepal length: "))
sw = float(input("Sepal width: "))
pl = float(input("Petal length: "))
pw = float(input("Petal width: "))

prediction = model.predict([[sl, sw, pl, pw]])[0]
print("Predicted species:", prediction)

plt.figure(figsize=(14,7))
plot_tree(model, feature_names=X.columns, class_names=model.classes_,
          filled=True, rounded=True)
plt.title("Decision Tree - Iris Classification")
plt.show()
