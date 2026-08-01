import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
data=pd.read_csv("data.csv")
stop_words={"the","and","is","a","an","to","of","was","with","in","for","on"}
text=" ".join(data["feedback"]).lower()
for ch in ".,!?":
    text=text.replace(ch,"")
words=[w for w in text.split() if w not in stop_words]
freq=Counter(words)
n=int(input("Enter Top N Words: "))
top=freq.most_common(n)
df=pd.DataFrame(top,columns=["Word","Frequency"])
print(df)
plt.figure(figsize=(7,4))
plt.bar(df["Word"],df["Frequency"])
plt.title("Top Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.show()