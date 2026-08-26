# Global Sales Data Analysis

A Python-based data analytics project that analyzes global sales records to identify patterns in revenue, profit, product performance, regional sales, and shipping efficiency.

## 📊 Project Overview

This project performs data cleaning, feature engineering, exploratory data analysis (EDA), and data visualization on a global sales dataset containing 21,540 records.

The analysis focuses on understanding sales performance across different regions and product categories and examining shipping lead time based on order priority.

## 🎯 Objectives

- Analyze overall sales and profit performance
- Compare revenue and profit across regions
- Identify high-performing product categories
- Analyze shipping lead time by order priority
- Calculate profit margin
- Explore relationships between numerical sales variables
- Create meaningful visualizations from the analysis

## 📁 Dataset

- **Records:** 21,540
- **Dataset:** Global Sales Records
- **Format:** CSV

The dataset contains sales-related information including order dates, shipping dates, regions, item types, units sold, unit price, unit cost, total revenue, total cost, and total profit.

## 🧹 Data Cleaning & Feature Engineering

The project uses Pandas to prepare the data for analysis.

The following steps were performed:

- Converted `Order Date` and `Ship Date` into datetime format
- Calculated `Ship Days`
- Calculated `Profit Margin (%)`
- Extracted `Order Year`
- Checked for missing values
- Checked for duplicate records
- Generated descriptive statistics

## 🔎 Exploratory Data Analysis

The analysis includes:

### Regional Analysis
Revenue, total profit, units sold, and profit margin were aggregated by region.

### Product Category Analysis
Revenue, total profit, units sold, and profit margin were analyzed for each product category.

### Order Priority Analysis
Average shipping days were analyzed for different order priority levels.

## 📈 Visualizations

The project contains four visualizations:

1. **Total Profit by Product Category**  
   Bar chart comparing total profit across product categories.

2. **Revenue Share by Region**  
   Pie chart showing the contribution of different regions to total revenue.

3. **Shipping Lead Time by Order Priority**  
   Box plot showing shipping days across different order priority levels.

4. **Correlation Heatmap**  
   Heatmap showing correlations between numerical sales variables such as units sold, unit price, unit cost, revenue, cost, profit, and shipping days.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## 📂 Project Structure

```text
Global-Sales-Data-Analysis/
│
├── dataset/
│   └── 50000_Sales_Records_21540.csv
│
├── plots/
│   ├── 1_profit_by_product.png
│   ├── 2_revenue_by_region.png
│   ├── 3_shipping_days.png
│   └── 4_correlation_heatmap.png
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore'''
