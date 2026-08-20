# Question:
# 19. Scenario: Analyze customer reviews for a product.
# Develop a Python program to calculate the frequency distribution of words
# in the customer reviews dataset.
# The program must take CSV input.

import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-19_customer_reviews.csv")

all_words = []

for review in data["review"].dropna():
    words = re.findall(r"\b[a-zA-Z]+\b", review.lower())
    all_words.extend(words)

frequency = Counter(all_words)

print("Word frequency distribution:")
for word, count in frequency.most_common():
    print(f"{word}: {count}")

top_words = frequency.most_common(10)
labels = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.bar(labels, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Words in Customer Reviews")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
