# Superstore Sales Analysis 📊

## 📌 Overview
This project is an **end-to-end sales data analysis** of the Sample Superstore dataset using **Python, Pandas, Matplotlib, and Plotly**.  
The goal was to explore sales performance, profitability, and regional trends through data cleaning, transformation, and insightful visualizations.

---

## 🛠 Tools & Technologies
- **Python 3.13**
- **Pandas** – Data manipulation
- **Matplotlib / Seaborn** – Static visualizations
- **Plotly Express** – Interactive maps
- **Visual Studio Code** – Development environment

---

## 📂 Dataset
- **Source:** Kaggle – [Sample Superstore Dataset](https://www.kaggle.com/datasets/blank/sample-superstore) *(replace link if needed)*
- **Description:** Contains sales transactions with attributes like `Order Date`, `Ship Date`, `Category`, `Segment`, `Region`, `Sales`, and `Profit`.

---

## 📊 Visualizations

### 1. Monthly Sales Trend
Identifies seasonality and monthly sales fluctuations.  
![Monthly Sales Trend](https://github.com/Soul-sketch/Superstore-Sales-Analysis/blob/main/Images/Monthly%20Sales%20Trend(2015-2018).png)

---

### 2. Sales by Category and Sub-Category
Shows which product lines drive the most revenue.  
![Sales by Category](https://github.com/Soul-sketch/Superstore-Sales-Analysis/blob/main/Images/Sales%20by%20Sub-Category%20and%20Category.png)

---

### 3. Top 10 Products by Sales
Highlights best-selling products for better inventory decisions.  
![Top Products](https://github.com/Soul-sketch/Superstore-Sales-Analysis/blob/main/Images/Top%2010%20Products%20by%20Sales.png)

---

### 4. Sales vs Profit by Segment
Compares revenue and profit distribution across customer segments.  
![Sales vs Profit by Segment](https://github.com/Soul-sketch/Superstore-Sales-Analysis/blob/main/Images/Sales%20vs%20Profit%20by%20Segment.png)

---

### 5. Sales by Region (Map)
Interactive geographical distribution of sales.  
![Sales by Region](https://github.com/Soul-sketch/Superstore-Sales-Analysis/blob/main/Images/Sales%20by%20region_Map.png)

---

## 📜 Code Explanation
The notebook is divided into:
1. **Data Loading & Cleaning**
   * Removed duplicates and handled missing values.
   * Parsed Order Date and Ship Date into datetime format.
   * Verified data types for accurate processing.
2. **Exploratory Data Analysis (EDA)**
   * Generated summary statistics.
   * Checked trends, seasonal patterns, and data distributions.
3. **Visualization**
   * Created static visualizations with Matplotlib & Seaborn.
   * Built an interactive US sales map with Plotly.
4. **Insights & Recommendations**
   * Extracted actionable business insights from the analysis.
---

## 💡 Insights Derived
- **Seasonality:** Peak sales observed in Q4, especially during November–December.
- **Profitability:** Certain sub-categories (e.g., Tables) generate high sales but low/negative profit margins.
- **Regional Trends:** The West region leads in sales, while the South has growth potential.
- **Customer Segments:** Consumer segment generates the highest revenue.

---

## 📌 How to Run
# Clone the repository
git clone https://github.com/Soul-sketch/Superstore-Sales-Analysis.git

# Navigate into the project folder
cd Superstore-Sales-Analysis

# Open and run the Python script
python Superstore_Analysis.py

---

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
