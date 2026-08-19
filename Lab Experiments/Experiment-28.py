import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeRegressor, plot_tree, export_text

df = pd.read_csv("cars.csv")

X = df[["mileage", "age", "brand", "engine_type"]]
y = df["price"]

preprocessor = ColumnTransformer(
    [("cat", OneHotEncoder(handle_unknown="ignore"), ["brand", "engine_type"])],
    remainder="passthrough"
)
X_enc = preprocessor.fit_transform(X)
feature_names = preprocessor.get_feature_names_out()

model = DecisionTreeRegressor(max_depth=4, random_state=42)
model.fit(X_enc, y)

print("Enter details of the car:")
mileage = float(input("Mileage: "))
age = float(input("Age in years: "))
brand = input("Brand: ")
engine_type = input("Engine type (Petrol/Diesel): ")

new_car = pd.DataFrame([[mileage, age, brand, engine_type]],
                       columns=["mileage", "age", "brand", "engine_type"])
new_enc = preprocessor.transform(new_car)
prediction = model.predict(new_enc)[0]

print(f"\nPredicted price = {prediction:.2f}")

print("\nDecision path:")
print(export_text(model, feature_names=list(feature_names)))

# Show tree
plt.figure(figsize=(16,8))
plot_tree(model, feature_names=feature_names, filled=True, rounded=True)
plt.title("CART Decision Tree for Car Price Prediction")
plt.show()
