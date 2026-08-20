# Question:
# Read the soccer-player CSV, find the top 5 by goals and salary, calculate
# average age, display players above average age, and visualize positions.
# Input: Exp-27_soccer_players.csv

import pandas as pd
import matplotlib.pyplot as plt

d=pd.read_csv("Exp-27_soccer_players.csv")
print("Top 5 goals:"); print(d.nlargest(5,"goals")[["name","goals"]])
print("\nTop 5 salaries:"); print(d.nlargest(5,"weekly_salary")[["name","weekly_salary"]])
avg=d.age.mean(); print("\nAverage age:",avg)
print("\nAbove average age:"); print(d.loc[d.age>avg,["name","age"]])
d.position.value_counts().plot(kind="bar")
plt.xlabel("Position"); plt.ylabel("Number of Players"); plt.title("Players by Position")
plt.tight_layout(); plt.show()
