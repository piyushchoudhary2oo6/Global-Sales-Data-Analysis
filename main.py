# ==============================================================================
# BEGINNER-FRIENDLY DATA ANALYTICS PROJECT IN PYTHON
# Dataset: Global Sales Records (21,540 rows)
# Required Libraries: pandas, matplotlib, seaborn
# ==============================================================================

import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set visual style for plots
sns.set_theme(style="whitegrid")

# ------------------------------------------------------------------------------
# STEP 1: LOAD AND INSPECT THE DATASET
# ------------------------------------------------------------------------------
print("--- STEP 1: Loading Dataset ---")

# Load the dataset using Pandas
file_name = "dataset/50000_Sales_Records_21540.csv"
df = pd.read_csv(file_name)

# Display basic information
print("\nFirst 5 rows of the dataset:")
print(df.head())

print("\nDataset Shape (Rows, Columns):", df.shape)

print("\nData Types and Missing Values:")
print(df.info())

print("\nCheck for Missing Values in each column:")
print(df.isnull().sum())

print("\nCheck for Duplicate Rows:")
print("Duplicate count:", df.duplicated().sum())


# ------------------------------------------------------------------------------
# STEP 2: DATA CLEANING AND FEATURE ENGINEERING
# ------------------------------------------------------------------------------
print("\n--- STEP 2: Data Cleaning & Feature Engineering ---")

# 1. Convert Date columns from text (object) to datetime format
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# 2. Calculate Shipping Days (Ship Date minus Order Date)
df["Ship Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# 3. Calculate Profit Margin Percentage
df["Profit Margin (%)"] = (df["Total Profit"] / df["Total Revenue"]) * 100

# 4. Extract Year from Order Date
df["Order Year"] = df["Order Date"].dt.year

print("Data Cleaning Complete. Newly added features:")
print(df[["Ship Days", "Profit Margin (%)", "Order Year"]].head())


# ------------------------------------------------------------------------------
# STEP 3: EXPLORATORY DATA ANALYSIS (SUMMARY TABLES)
# ------------------------------------------------------------------------------
print("\n--- STEP 3: Exploratory Data Analysis ---")

# Summary statistics for numerical columns
print("\nDescriptive Statistics:")
print(df.describe())

# Group by Region to see Revenue and Profit
print("\nSales Performance by Region:")
region_summary = (
    df.groupby("Region")[["Total Revenue", "Total Profit", "Units Sold"]]
    .sum()
    .reset_index()
)
region_summary["Profit Margin (%)"] = (
    region_summary["Total Profit"] / region_summary["Total Revenue"]
) * 100
print(region_summary.sort_values(by="Total Revenue", ascending=False))

# Group by Item Type (Product Category)
print("\nSales Performance by Product Category (Item Type):")
item_summary = (
    df.groupby("Item Type")[["Total Revenue", "Total Profit", "Units Sold"]]
    .sum()
    .reset_index()
)
item_summary["Profit Margin (%)"] = (
    item_summary["Total Profit"] / item_summary["Total Revenue"]
) * 100
print(item_summary.sort_values(by="Total Profit", ascending=False))

# Group by Order Priority to check average shipping days
print("\nAverage Shipping Days by Order Priority:")
priority_summary = (
    df.groupby("Order Priority")["Ship Days"].mean().reset_index()
)
print(priority_summary)


# ------------------------------------------------------------------------------
# STEP 4: CREATE VISUALIZATIONS
# ------------------------------------------------------------------------------
print("\n--- STEP 4: Creating Visualizations ---")

# Create a folder to save plots if it doesn't exist
output_folder = "plots"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# CHART 1: Total Profit by Product Category (Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(
    data=item_summary, x="Total Profit", y="Item Type", palette="Blues_r"
)
plt.title("Total Profit by Product Category")
plt.xlabel("Total Profit ($)")
plt.ylabel("Product Category")
plt.tight_layout()
plt.savefig(f"{output_folder}/1_profit_by_product.png")
plt.show()

# CHART 2: Revenue Distribution by Region (Pie Chart)
plt.figure(figsize=(8, 8))
plt.pie(
    region_summary["Total Revenue"],
    labels=region_summary["Region"],
    autopct="%1.1f%%",
    startangle=140,
)
plt.title("Revenue Share by Region")
plt.tight_layout()
plt.savefig(f"{output_folder}/2_revenue_by_region.png")
plt.show()

# CHART 3: Shipping Days by Order Priority (Box Plot)
plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Order Priority",
    y="Ship Days",
    order=["L", "M", "H", "C"],
    palette="Set2",
)
plt.title("Shipping Lead Time by Order Priority")
plt.xlabel("Order Priority (L=Low, M=Medium, H=High, C=Critical)")
plt.ylabel("Days to Ship")
plt.tight_layout()
plt.savefig(f"{output_folder}/3_shipping_days.png")
plt.show()

# CHART 4: Correlation Heatmap
plt.figure(figsize=(8, 6))
numeric_columns = [
    "Units Sold",
    "Unit Price",
    "Unit Cost",
    "Total Revenue",
    "Total Cost",
    "Total Profit",
    "Ship Days",
]
sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(f"{output_folder}/4_correlation_heatmap.png")
plt.show()

print(
    f"\nAll plots created successfully and saved in the '{output_folder}' directory!"
)