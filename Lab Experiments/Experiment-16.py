from collections import Counter
import matplotlib.pyplot as plt
with open("sample_text.txt","r") as file:
    text=file.read().lower()
words=text.replace(".","").replace(",","").split()
freq=Counter(words)
print(freq)
plt.figure(figsize=(6,4))
plt.bar(freq.keys(),freq.values())
plt.title("Word Frequency")
plt.xlabel("Words")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()