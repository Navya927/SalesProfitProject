import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create images folder
os.makedirs("images", exist_ok=True)

# Load dataset
df = pd.read_excel("data/sample_-_superstore.xls")

print("Dataset Loaded Successfully!")
print("Dataset Shape:", df.shape)

# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6, 4))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/sales_by_category.png")
plt.close()

print("✓ Sales by Category graph saved")

# 2. Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(6, 4))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("images/profit_by_category.png")
plt.close()

print("✓ Profit by Category graph saved")

# 3. Top 10 Products by Sales
top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_products.plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales")
plt.tight_layout()
plt.savefig("images/top_products.png")
plt.close()

print("✓ Top Products graph saved")

# 4. Monthly Sales Trend
df["Order Date"] = pd.to_datetime(df["Order Date"])

monthly_sales = (
    df.groupby(df["Order Date"].dt.to_period("M"))["Sales"]
    .sum()
)

plt.figure(figsize=(10, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/monthly_sales_trend.png")
plt.close()

print("✓ Monthly Sales Trend graph saved")

# 5. Correlation Heatmap
numeric_df = df.select_dtypes(include=["number"])

plt.figure(figsize=(10, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("images/correlation_heatmap.png")
plt.close()

print("✓ Correlation Heatmap saved")

print("\nAll graphs saved successfully inside the images folder!")