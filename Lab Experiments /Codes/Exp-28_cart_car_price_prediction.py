# Question:
# Use CART regression from scikit-learn to predict a used-car price from
# mileage, age, brand and engine type. Allow user input and display the
# learned decision-tree rules.
# Input: Exp-28_car_prices.csv

import pandas as pd
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

d=pd.read_csv("Exp-28_car_prices.csv")
X=d[["mileage","age","brand","engine_type"]]; y=d.price
pre=ColumnTransformer([("cat",OneHotEncoder(handle_unknown="ignore"),["brand","engine_type"])],remainder="passthrough")
Xt=pre.fit_transform(X)
model=DecisionTreeRegressor(max_depth=4,random_state=42).fit(Xt,y)
mileage=float(input("Mileage (km): ")); age=float(input("Age (years): "))
brand=input("Brand: "); engine=input("Engine type (Petrol/Diesel/Electric): ")
new=pd.DataFrame([{"mileage":mileage,"age":age,"brand":brand,"engine_type":engine}])
pred=model.predict(pre.transform(new))[0]
print("Predicted price:",pred)
print("\nDecision tree rules:")
print(export_text(model,feature_names=list(pre.get_feature_names_out())))
