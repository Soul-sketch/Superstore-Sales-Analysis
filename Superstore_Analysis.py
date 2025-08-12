import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Python Files\Cleaned_Superstore.csv")

# Parse dates
df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors="raise")
df['Ship Date'] = pd.to_datetime(df['Ship Date'], dayfirst=True,  errors="raise")

# Quick confirmation
print("All Order Dates parsed:", df['Order Date'].notnull().all())
print("All Ship Dates parsed:", df['Ship Date'].notnull().all())

# KPI Analysis

print("\n====== SUPERSTORE KPIs ======\n")

# Total Sales
total_sales = df['Sales'].sum()

# Total profit
total_profit = df['Profit'].sum()

# Average Discount
avg_discount = df['Discount'].mean()

# Total Orders
total_orders = df['Order ID'].nunique()

# Top 5 Products by Sales
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(5)

# Print KPIs
print("Total Sales: ${:,.2f}".format(total_sales))
print("Total Profit: ${:,.2f}".format(total_profit))
print("Average Discount: {:.2%}".format(avg_discount))
print("Total Orders:", total_orders)
print("\nTop 5 products by Sales:\n", top_products)

# Data Cleaning

print("\n====== DATA ClEANING ======\n")

# Ensure datetime format
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Drop rows where Order Date couldn't be converted
df = df.dropna(subset=['Order Date'])

# Filter realistic date range
df = df[(df['Order Date'] >= '2015-01-01') & (df['Order Date'] <= '2018-12-31')]

# Sanity Check
print("Min Date:", df['Order Date'].min())
print("Max Date:", df['Order Date'].max())

# Visualizations

print("\n====== VISUALIZATIONS ======\n")

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.patches as patches
import seaborn as sns
import plotly.express as px

# Group by month and sum sales
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M')).sum(numeric_only=True)['Sales']
monthly_sales.index = monthly_sales.index.to_timestamp()

# Plot monthly sales
plt.figure(figsize=(14, 6))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='skyblue', linewidth=2)

# Format x-axis: Month abbrivation + Year
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b-%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3)) # Show every 3 months for clarity
plt.xticks(rotation=45)

# Add date labels
for x, y in zip(monthly_sales.index, monthly_sales.values):
    plt.text(x, y, f'{y:,.0f}', ha='center', va='bottom', fontsize=8, rotation=45)

# Titles and Labels
plt.title('Monthly Sales Trend(2015-2018)', fontsize=16, fontweight='bold')
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sales ($)', fontsize=12)
plt.grid(visible=True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show() 

# Sales by Category and Sub-Category

# Group and sort data by Category and Sub-Category
category_sales = df.groupby(['Category', 'Sub-Category'])['Sales'].sum().reset_index()
category_sales = category_sales.sort_values(['Category', 'Sales'], ascending=[True, False])

# Create figure 
plt.figure(figsize=(12, 7))
colors = {'Furniture': '#1f77b4', 'Office Supplies': '#ff7f0e', 'Technology': '#2ca02c'}

# Plot bars
bars = plt.barh(category_sales['Sub-Category'], category_sales['Sales'], color=[colors[cat] for cat in category_sales['Category']])

# Highlight top sub-category overall
top_index = category_sales['Sales'].idxmax()
bars[category_sales.index.get_loc(top_index)].set_color('#d62728') # Deep red for emphasis

# Add value labels with better spacing
for bar in bars:
    width = bar.get_width()
    plt.text(width + 200, bar.get_y() + bar.get_height() / 2, f'${width:,.0f}', va='center', fontsize=10) # Nudeged further from bar

# Labels & title
plt.xlabel('Sales ($)', fontsize=12, labelpad=10)
plt.ylabel('Sub-Category', fontsize=12)
plt.title('Sales by Sub-Category', fontsize=16, pad=15)

# Legend repostioned to bottom
from matplotlib.patches import Patch
legend_handles = [Patch(color=color, label=cat) for cat, color in colors.items()]
plt.legend(handles=legend_handles, title='Category', loc='upper center', bbox_to_anchor=(0.5, -0.08), ncol=3)

# Style adjustments
plt.gca().invert_yaxis() # largest at top within each category
plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# Top 10 Products by Sales

# Assuming 'df' is already loaded and cleaned
# Group by Product Name and sum sales
top_products = df.groupby('Product Name')['Sales'].sum().reset_index()

# Sort and select top 10
top_products = top_products.sort_values(by='Sales', ascending=False).head(10)

# Set style
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))

# Create barplot
ax = sns.barplot(
    x='Sales', 
    y='Product Name', 
    data=top_products, 
    palette='Blues_r'
)

# Format labels with $ sign and commas
for i, value in enumerate(top_products['Sales']):
    ax.text(
        value + 50,   # offset for visibility
        i, 
        f"${value:,.2f}", 
        va='center', 
        fontsize=10
    )

# Title and labels
plt.title("Top 10 Products by Sales", fontsize=16, fontweight='bold')
plt.xlabel("Total Sales (USD)", fontsize=12)
plt.ylabel("Product Name", fontsize=12)

plt.tight_layout()
plt.show()

# Sales vs Profit by Segment

# Group data by Segment and aggregate Sales and Profit
sales_profit_segment = df.groupby('Segment')[['Sales', 'Profit']].sum().reset_index()

# Create figure
plt.figure(figsize=(10, 6))
bar_width = 0.4
x = range(len(sales_profit_segment))

# Bars for sales
plt.bar(x, sales_profit_segment['Sales'], width=bar_width, label='Sales', color='#4C7280')

# Bars for profit (shifted to the right)
plt.bar([i + bar_width for i in x], sales_profit_segment['Profit'], width=bar_width, label='Profit', color='#55A868')

# Add value labels with $ sign above each bar
for p in plt.gca().patches:
    height = p.get_height()
    if height > 0:  # Avoid labeling bars with zero height
        plt.annotate(
            f"${height:,.0f}",
            (p.get_x() + p.get_width() / 2., height),
            ha='center',
            va='bottom',
            fontsize=10,
            color='black',
            xytext=(0, 6),
            textcoords='offset points'
        )

# Titles and labels
plt.title('Sales vs Profit by Segment', fontsize=16, fontweight='bold')
plt.xlabel('Segment', fontsize=12)
plt.ylabel('Sales and Profit ($)', fontsize=12)
plt.xticks([i + bar_width/2 for i in x], sales_profit_segment['Segment'])
plt.legend()

# force plain style (no scientific notation) on y-axis
plt.ticklabel_format(style='plain', axis='y')

# Grid and layout
plt.grid(axis='y', linestyle='--', alpha=0.7, color='lightgrey', zorder=0) 
plt.tight_layout()
plt.show()


# Sales by Region

# Group sales by Region and State for better mapping
sales_state = df.groupby(['State', 'Region'])['Sales'].sum().reset_index()

# Map each state to its two-letter code (needed for US maps)
state_abbreviations = {'Alabama': 'AL', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO',
                       'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'District of Columbia': 'DC',
                       'Florida': 'FL', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
                       'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
                       'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
                       'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
                       'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
                       'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD',
                       'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA',
                       'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY'  }

sales_state['State Code'] = sales_state['State'].map(state_abbreviations)

# Create the map chart
fig = px.choropleth(
    sales_state,
    locations='State Code',
    locationmode='USA-states',
    color='Sales',
    scope="usa",
    hover_name='State',
    hover_data=['Region', 'Sales'],
    color_continuous_scale='Blues',
    labels={'Sales': 'Sales ($)'}
)

fig.update_layout(title_text='Sales by Region (US Map)', title_x = 0.5, geo=dict(showframe=False, showcoastlines=False))

fig.show()