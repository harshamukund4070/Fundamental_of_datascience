# Question:
# 13. Scenario: Analyze the variability of stock prices for a company.
# The stock data includes closing prices for each trading day.
# Read stock data from a CSV file, calculate the variability of stock prices,
# and provide insights into the stock's price movements.
# The program must take CSV input.

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Exp-13_stock_data.csv")
prices = data["closing_price"]

mean_price = prices.mean()
variance = prices.var()
std_deviation = prices.std()
minimum = prices.min()
maximum = prices.max()
price_range = maximum - minimum

print(f"Mean closing price: {mean_price:.2f}")
print(f"Variance: {variance:.2f}")
print(f"Standard deviation: {std_deviation:.2f}")
print(f"Minimum closing price: {minimum:.2f}")
print(f"Maximum closing price: {maximum:.2f}")
print(f"Price range: {price_range:.2f}")

if std_deviation < mean_price * 0.05:
    print("Insight: Stock price variability is relatively low.")
else:
    print("Insight: Stock price variability is relatively high.")

plt.plot(data["date"], prices, marker="o")
plt.xlabel("Trading Date")
plt.ylabel("Closing Price")
plt.title("Stock Closing Price Movement")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
