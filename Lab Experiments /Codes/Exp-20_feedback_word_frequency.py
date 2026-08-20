# Question:
# 20. Scenario: Analyze customer feedback from social media platforms.
# Requirements:
# - Load data.csv containing a single column named "feedback".
# - Remove punctuation.
# - Convert text to lowercase.
# - Eliminate stop words.
# - Calculate word frequency distribution.
# - Display the top N most frequent words and frequencies, where N is user input.
# - Plot a bar graph of the top N words.
# The program must take CSV input.

import pandas as pd
import re
from collections import Counter
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-20_data.csv")

stop_words = {
    "the", "and", "is", "a", "an", "to", "of", "in", "on", "for",
    "with", "this", "that", "it", "was", "are", "be", "as", "at",
    "by", "from", "or", "but", "very", "i", "we", "you", "they"
}

all_words = []

for feedback in data["feedback"].dropna():
    text = feedback.lower()
    words = re.findall(r"\b[a-zA-Z]+\b", text)
    words = [word for word in words if word not in stop_words]
    all_words.extend(words)

frequency = Counter(all_words)

n = int(input("Enter N (number of top words): "))
top_words = frequency.most_common(n)

print(f"\nTop {n} most frequent words:")
for word, count in top_words:
    print(f"{word}: {count}")

labels = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.bar(labels, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title(f"Top {n} Words in Customer Feedback")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
