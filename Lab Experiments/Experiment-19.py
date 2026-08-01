import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
data=pd.read_csv("customer_reviews.csv")
text=" ".join(data["Review"]).lower()
words=text.replace(".","").replace(",","").split()
freq=Counter(words)
print(freq)
plt.figure(figsize=(7,4))
plt.bar(freq.keys(),freq.values())
plt.title("Customer Review Word Frequency")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()