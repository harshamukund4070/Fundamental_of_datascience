# Question:
# 18. Scenario: Analyze social media user interaction data.
# The dataset contains the number of likes received by each post.
# Develop a Python program to calculate the frequency distribution of likes among posts.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-18_post_likes.csv")

like_frequency = data["likes"].value_counts().sort_index()

print("Frequency distribution of likes:")
print(like_frequency)

plt.bar(like_frequency.index.astype(str), like_frequency.values)
plt.xlabel("Number of Likes")
plt.ylabel("Number of Posts")
plt.title("Frequency Distribution of Likes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
