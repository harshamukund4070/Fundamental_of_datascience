# Question:
# Scenario: Analyze fuel efficiency of different car models.
# Calculate the average fuel efficiency and determine the percentage improvement
# in fuel efficiency between two car models.
# The program must take CSV input.

import numpy as np
import matplotlib.pyplot as plt

fuel_efficiency = np.loadtxt("Exp-5_fuel_efficiency.csv", delimiter=",", skiprows=1)
efficiency = fuel_efficiency[:, 0]

average_efficiency = np.mean(efficiency)

model1 = efficiency[0]
model2 = efficiency[1]
percentage_improvement = ((model2 - model1) / model1) * 100

print(f"Average fuel efficiency: {average_efficiency:.2f} MPG")
print(f"Percentage improvement from Model 1 to Model 2: {percentage_improvement:.2f}%")

plt.bar(["Model 1", "Model 2"], [model1, model2])
plt.ylabel("Fuel Efficiency (MPG)")
plt.title("Fuel Efficiency Comparison")
plt.tight_layout()
plt.show()
