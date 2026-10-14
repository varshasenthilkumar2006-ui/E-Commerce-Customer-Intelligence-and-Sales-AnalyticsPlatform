import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / "Dataset" / "ecommerce_advanced.csv"

df = pd.read_csv(csv_path)

print("✅ Dataset Loaded Successfully!")
print("Shape:", df.shape)
print(df.head())
print(df["Category"].value_counts())
print(df[["Sales", "Profit"]].head(10))






# -------------------------------
# Data Cleaning
# -------------------------------

print("\n========== DATA CLEANING ==========")

print("Missing Values:")
print(df.isnull().sum())

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print("Shape:", df.shape)

df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

print("\nData Types:")
print(df.dtypes)

print("\nCleaned Dataset:")
print(df.head())

# Display data types
print(df.dtypes)

# -------------------------------
# Analysis starts here
# -------------------------------

print(df.head())

print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

# ==========================
# KPI CALCULATIONS
# ==========================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
total_products = df["Product_Name"].nunique()
average_order_value = df["Sales"].mean()

print("\n========== KPI DASHBOARD ==========")
print(f"Total Sales        : ₹{total_sales}")
print(f"Total Profit       : ₹{total_profit}")
print(f"Total Orders       : {total_orders}")
print(f"Unique Products    : {total_products}")
print(f"Average Order Value: ₹{average_order_value:.2f}")
# ==========================
# TOP 10 MOST PROFITABLE PRODUCTS
# ==========================

print("\n========== TOP 10 MOST PROFITABLE PRODUCTS ==========")

top_profit = df.groupby("Product_Name")["Profit"].sum().sort_values(ascending=False)

print(top_profit.head(10))




# Display first 5 rows
print("========== FIRST 5 RECORDS ==========")
print(df.head())

# Dataset information
print("\n========== DATASET INFO ==========")
print(df.info())

# Check missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Basic statistics
print("\n========== SUMMARY ==========")
print(df.describe())

# Total Sales
print("\n========== TOTAL SALES ==========")
print("₹", df["Sales"].sum())

# Total Profit
print("\n========== TOTAL PROFIT ==========")
print("₹", df["Profit"].sum())

import matplotlib.pyplot as plt

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()
print(category_sales)
print(df["Category"].unique())
print(df["Category"].isnull().sum())
print(df["Category"].head(20))


plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.savefig("dashboard.png", dpi=300)
plt.savefig("Images/monthly_sales.png")

plt.show()

# State-wise Sales Pie Chart
state_sales = df.groupby("State")["Sales"].sum()

plt.figure(figsize=(7,7))
plt.pie(state_sales, labels=state_sales.index, autopct="%1.1f%%", startangle=90)

plt.title("State-wise Sales Distribution")
plt.savefig("dashboard.png", dpi=300)
plt.savefig("Imagesmonthly_sales.png")

plt.show()

# State-wise Sales Line Chart
state_sales = df.groupby("State")["Sales"].sum()

plt.figure(figsize=(8,5))
plt.plot(state_sales.index, state_sales.values, marker="o", linewidth=2)

plt.title("State-wise Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("dashboard.png", dpi=300)
plt.savefig("Images/monthly_sales.png")

plt.close()

# Scatter Plot
plt.figure(figsize=(8,5))

plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.savefig("dashboard.png", dpi=300)
plt.savefig("Images/monthly_sales.png")

plt.close()

# Histogram
plt.figure(figsize=(8,5))

plt.hist(df["Sales"], bins=5)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("dashboard.png", dpi=300)
plt.savefig("Images/monthly_sales.png")

plt.close()

# Histogram
plt.figure(figsize=(8,5))

plt.hist(df["Sales"], bins=5)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.grid(True)
plt.savefig("dashboard.png", dpi=300)
plt.savefig("Images/monthly_sales.png")

plt.close()

print("\n========== BUSINESS INSIGHTS ==========")

print("Highest Sales :", df.loc[df["Sales"].idxmax(), "Product_Name"])
print("Highest Profit :", df.loc[df["Profit"].idxmax(), "Product_Name"])

print("\nCategory Wise Sales")
print(df.groupby("Category")["Sales"].sum())

print("\nState Wise Sales")
print(df.groupby("State")["Sales"].sum())
print("\n========== ADVANCED KPI ANALYSIS ==========")

# Top 10 Products by Sales
top_products = df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False)

print("\nTop 10 Products")
print(top_products.head(10))

# Top 10 States
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False)

print("\nTop 10 States")
print(top_states.head(10))

# Average Profit
print("\nAverage Profit :", round(df["Profit"].mean(), 2))

# Highest Sale
print("Highest Sale :", df["Sales"].max())

# Total Orders
print("Total Orders :", len(df))
plt.figure(figsize=(12,6))

top_products.head(10).plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.savefig("Images/monthly_sales.png")

plt.close()
# Convert Order_Date to datetime
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create Month column
df["Month"] = df["Order_Date"].dt.to_period("M")

# Monthly Sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)
plt.figure(figsize=(12,6))

monthly_sales.plot(
    kind="line",
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.savefig("Images/monthly_sales.png")

plt.close()
# Customer-wise Sales

customer_sales = df.groupby("Customer_Name")["Sales"].sum().sort_values(ascending=False)

print("\n========== TOP 10 CUSTOMERS ==========")
print(customer_sales.head(10))
plt.figure(figsize=(12,6))

customer_sales.head(10).plot(kind="bar")

plt.title("Top 10 Customers by Sales")
plt.xlabel("Customer Name")
plt.ylabel("Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Images/monthly_sales.png")
plt.close()
print("\n========== CORRELATION MATRIX ==========")

correlation = df[["Sales", "Profit", "Quantity"]].corr()

print(correlation)
plt.figure(figsize=(6,5))

plt.imshow(correlation, cmap="Blues")

plt.xticks(range(len(correlation.columns)), correlation.columns)
plt.yticks(range(len(correlation.columns)), correlation.columns)

plt.colorbar()
plt.title("Correlation Matrix")
plt.savefig("Images/monthly_sales.png")

plt.close()
# ==========================
# SIMPLE SALES FORECAST
# ==========================

average_sales = df["Sales"].mean()

print("\n========== SALES FORECAST ==========")

for month in range(1, 4):
    predicted_sales = average_sales * (1 + (0.05 * month))
    print(f"Predicted Sales for Next Month {month}: ₹{predicted_sales:.2f}")
    forecast = []

for month in range(1, 4):
    forecast.append(average_sales * (1 + (0.05 * month)))

plt.figure(figsize=(8,5))

plt.plot(
    ["Next Month 1", "Next Month 2", "Next Month 3"],
    forecast,
    marker="o"
)

plt.title("Sales Forecast")
plt.xlabel("Future Months")
plt.ylabel("Predicted Sales")

plt.grid(True)
plt.savefig("Images/monthly_sales.png")

plt.close()
print("\n========== BUSINESS INSIGHTS ==========")

# Highest Sales Product
highest_sales_product = df.loc[df["Sales"].idxmax(), "Product_Name"]
print(f"Highest Selling Product : {highest_sales_product}")

# Highest Profit Product
highest_profit_product = df.loc[df["Profit"].idxmax(), "Product_Name"]
print(f"Highest Profit Product : {highest_profit_product}")

# Top State
top_state = df.groupby("State")["Sales"].sum().idxmax()
print(f"Top Performing State : {top_state}")

# Best Category
best_category = df.groupby("Category")["Sales"].sum().idxmax()
print(f"Best Category : {best_category}")

print("\nBusiness Recommendation:")
print("- Increase stock for best-selling products.")
print("- Focus marketing in the top-performing state.")
print("- Promote high-profit products.")
print("- Improve sales in low-performing categories.")
# ==========================
# EXPORT REPORT TO EXCEL
# ==========================

summary = pd.DataFrame({
    "Metric": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Average Order Value"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_orders,
        average_order_value
    ]
})

summary.to_excel("Sales_Report.xlsx", index=False)

print("\n✅ Sales_Report.xlsx Created Successfully!")
