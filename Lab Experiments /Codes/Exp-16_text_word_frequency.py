# Question:
# 16. Scenario: Determine the frequency distribution of words in a text document.
# The text document is named "sample_text.txt".
# Develop a Python program to read the document, process the text,
# and calculate the frequency distribution of words.
# The program must take the text file as input.

import re
from collections import Counter
import matplotlib.pyplot as plt

with open("Exp-16_sample_text.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
frequency = Counter(words)

print("Word frequency distribution:")
for word, count in frequency.most_common():
    print(f"{word}: {count}")

top_words = frequency.most_common(10)
labels = [item[0] for item in top_words]
counts = [item[1] for item in top_words]

plt.bar(labels, counts)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Top 10 Word Frequencies")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
