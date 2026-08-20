# Question:
# Scenario: Analyze a real estate Pandas DataFrame named property_data.
# Find:
# 1. The average listing price of properties in each location.
# 2. The number of properties with more than four bedrooms.
# 3. The property with the largest area.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

property_data = pd.read_csv("Exp-9_property_data.csv")

average_price_by_location = property_data.groupby("location")["listing_price"].mean()
more_than_four_bedrooms = (property_data["bedrooms"] > 4).sum()
largest_property = property_data.loc[property_data["area_sqft"].idxmax()]

print("\nAverage listing price by location:")
print(average_price_by_location)

print("\nNumber of properties with more than 4 bedrooms:", more_than_four_bedrooms)

print("\nProperty with the largest area:")
print(largest_property)

average_price_by_location.plot(kind="bar")
plt.xlabel("Location")
plt.ylabel("Average Listing Price")
plt.title("Average Property Listing Price by Location")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()
