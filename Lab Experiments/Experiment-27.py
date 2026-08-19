import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("players.csv")

print("Top 5 players by goals:")
print(df.nlargest(5, "goals")[["name", "goals"]].to_string(index=False))

print("\nTop 5 players by weekly salary:")
print(df.nlargest(5, "weekly_salary")[["name", "weekly_salary"]].to_string(index=False))

avg_age = df["age"].mean()
print(f"\nAverage age = {avg_age:.2f}")

print("\nPlayers above average age:")
print(df.loc[df["age"] > avg_age, ["name", "age"]].to_string(index=False))

# Position distribution
position_counts = df["position"].value_counts()
position_counts.plot(kind="bar", figsize=(7,5))
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.title("Distribution of Players by Position")
plt.xticks(rotation=0)
plt.grid(axis="y", alpha=0.3)
plt.show()
