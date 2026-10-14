import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("Dataset/ecommerce_advanced.csv")

# Clean numeric columns
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce").fillna(0)

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# -------------------------------
# TITLE
# -------------------------------
st.title("🛒 E-Commerce Analytics Dashboard")
st.write("Sales, Profit and Customer Performance Analysis")

st.divider()
# -----------------------------
# FILTERS
# -----------------------------
st.subheader("🔎 Filters")

col1, col2 = st.columns(2)

with col1:
    selected_category = st.selectbox(
        "Select Category",
        ["All"] + sorted(df["Category"].dropna().unique().tolist())
    )

with col2:
    selected_state = st.selectbox(
        "Select State",
        ["All"] + sorted(df["State"].dropna().unique().tolist())
    )

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

if selected_state != "All":
    filtered_df = filtered_df[filtered_df["State"] == selected_state]
    # Date Filter
min_date = df["Order_Date"].min().date()
max_date = df["Order_Date"].max().date()

selected_dates = st.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    filtered_df = filtered_df[
        (filtered_df["Order_Date"].dt.date >= start_date) &
        (filtered_df["Order_Date"].dt.date <= end_date)
    ]
    # -----------------------------
# DOWNLOAD FILTERED DATA
# -----------------------------
st.subheader("📥 Download Data")

csv_data = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data",
    data=csv_data,
    file_name="filtered_ecommerce_data.csv",
    mime="text/csv"
)
# -----------------------------
# BUSINESS INSIGHTS
# -----------------------------
st.subheader("💡 Business Insights")

if not filtered_df.empty:

    best_category = (
        filtered_df.groupby("Category")["Sales"]
        .sum()
        .idxmax()
    )

    best_state = (
        filtered_df.groupby("State")["Sales"]
        .sum()
        .idxmax()
    )

    best_product = (
        filtered_df.groupby("Product_Name")["Sales"]
        .sum()
        .idxmax()
    )

    highest_profit_product = (
        filtered_df.groupby("Product_Name")["Profit"]
        .sum()
        .idxmax()
    )

    average_order_value = (
        filtered_df["Sales"].sum() /
        filtered_df["Order_ID"].nunique()
    )

    st.write(f"🏷️ **Best Selling Category:** {best_category}")
    st.write(f"📍 **Top Performing State:** {best_state}")
    st.write(f"🏆 **Best Selling Product:** {best_product}")
    st.write(f"💰 **Most Profitable Product:** {highest_profit_product}")
    st.write(f"🛒 **Average Order Value:** ₹{average_order_value:,.2f}")

else:
    st.warning("No data available for the selected filters.")

# -------------------------------
# KPI CARDS
# -------------------------------
total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order_ID"].nunique()
total_quantity = filtered_df["Quantity"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"₹{total_sales:,.2f}")
col2.metric("📈 Total Profit", f"₹{total_profit:,.2f}")
col3.metric("🛍️ Total Orders", total_orders)
col4.metric("📦 Quantity Sold", int(total_quantity))

st.divider()

# -------------------------------
# CATEGORY-WISE SALES
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Category-wise Sales")

    category_sales = filtered_df.groupby("Category")["Sales"].sum()

    fig, ax = plt.subplots(figsize=(7, 4))
    category_sales.plot(kind="bar", ax=ax)
    ax.set_xlabel("Category")
    ax.set_ylabel("Sales")
    ax.set_title("Category-wise Sales")
    plt.xticks(rotation=30)
    plt.tight_layout()

    st.pyplot(fig)
    # -----------------------------
# PROFIT BY CATEGORY
# -----------------------------
st.subheader("💰 Profit by Category")

category_profit = filtered_df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 4))
category_profit.plot(kind="bar", ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Profit")
ax.set_title("Profit by Category")

plt.xticks(rotation=30)
plt.tight_layout()

st.pyplot(fig)
# -----------------------------
# TOP 10 PROFITABLE PRODUCTS
# -----------------------------
st.subheader("🏆 Top 10 Most Profitable Products")

top_profit_products = (
    filtered_df.groupby("Product_Name")["Profit"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(10, 5))
top_profit_products.plot(kind="bar", ax=ax)

ax.set_xlabel("Product")
ax.set_ylabel("Profit")
ax.set_title("Top 10 Most Profitable Products")

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# -------------------------------
# STATE-WISE SALES
# -------------------------------
with col2:
    st.subheader("🗺️ State-wise Sales")

    state_sales = filtered_df.groupby("State")["Sales"].sum().sort_values(ascending=False)

    fig, ax = plt.subplots(figsize=(7, 4))
    state_sales.plot(kind="bar", ax=ax)
    ax.set_xlabel("State")
    ax.set_ylabel("Sales")
    ax.set_title("State-wise Sales")
    plt.xticks(rotation=90, fontsize=7)
    plt.tight_layout()

    st.pyplot(fig)

st.divider()

# -------------------------------
# MONTHLY SALES
# -------------------------------
st.subheader("📅 Monthly Sales Trend")

monthly_sales = (
    filtered_df.dropna(subset=["Order_Date"])
    .set_index("Order_Date")
    .resample("ME")["Sales"]
    .sum()
)

fig, ax = plt.subplots(figsize=(12, 4))
monthly_sales.plot(kind="line", marker="o", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
ax.set_title("Monthly Sales Trend")
plt.tight_layout()

st.pyplot(fig)

st.divider()

# -------------------------------
# SALES VS PROFIT
# -------------------------------
st.subheader("💹 Sales vs Profit")

fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(filtered_df["Sales"], filtered_df["Profit"], alpha=0.6)

ax.set_xlabel("Sales")
ax.set_ylabel("Profit")
ax.set_title("Sales vs Profit")

plt.tight_layout()

st.pyplot(fig)

st.divider()

# -------------------------------
# TOP PRODUCTS
# -------------------------------
st.subheader("🏆 Top 10 Products by Sales")

top_products = (
    filtered_df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(
    top_products.reset_index(),
    use_container_width=True
)

st.divider()

# -------------------------------
# DATA TABLE
# -------------------------------
st.subheader("📋 Dataset Preview")

st.dataframe(
    df.head(20),
    use_container_width=True
)

st.success("✅ E-Commerce Analytics Dashboard Loaded Successfully!")