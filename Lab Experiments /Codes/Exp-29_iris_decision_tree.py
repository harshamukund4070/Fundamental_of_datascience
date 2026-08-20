# Question:
# Load the Iris dataset from scikit-learn. Allow user input for sepal length,
# sepal width, petal length and petal width, then predict the flower species
# using a Decision Tree classifier.

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier,plot_tree
import numpy as np
import matplotlib.pyplot as plt

iris=load_iris()
model=DecisionTreeClassifier(max_depth=4,random_state=42).fit(iris.data,iris.target)
v=[float(input("Sepal length: ")),float(input("Sepal width: ")),
   float(input("Petal length: ")),float(input("Petal width: "))]
p=model.predict(np.array([v]))[0]
print("Predicted species:",iris.target_names[p])
plt.figure(figsize=(12,7))
plot_tree(model,feature_names=iris.feature_names,class_names=iris.target_names,filled=True)
plt.title("Iris Decision Tree"); plt.tight_layout(); plt.show()
