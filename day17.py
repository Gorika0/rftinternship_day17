import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Customer_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Age": [22, 35, 45, 25, 40, 30, 50, 28, 33, 60],
    "Spending": [2000, 5000, 7000, 1500, 6500, 3000, 8000, 2500, 4000, 9000],
    "Visits": [5, 12, 15, 3, 14, 7, 18, 4, 9, 20]
}

df = pd.DataFrame(data)
def segment_customer(spending):
    if spending >= 7000:
        return "High"
    elif spending >= 3000:
        return "Medium"
    else:
        return "Low"

df["Segment"] = df["Spending"].apply(segment_customer)

high_value = df[df["Spending"] >= 7000]
low_engagement = df[df["Visits"] < 5]

print("Customer Dataset")
print(df)

print("\nHigh Value Customers")
print(high_value)
print("\nLow Engagement Customers")
print(low_engagement)

plt.figure(figsize=(8,5))
plt.hist(df["Spending"], bins=5)
plt.title("Spending Distribution")
plt.xlabel("Spending Amount")
plt.ylabel("Number of Customers")
plt.show()

segment_count = df["Segment"].value_counts()
plt.figure(figsize=(6,5))
plt.pie(segment_count, labels=segment_count.index, autopct='%1.1f%%')
plt.title("Customer Categories")
plt.show()

print("\nBusiness Strategies")
print("1. Give premium offers to High-value customers.")
print("2. Provide discounts to Medium customers to increase spending.")
print("3. Send promotional messages to Low customers.")
print("4. Improve engagement for customers with fewer visits.")
