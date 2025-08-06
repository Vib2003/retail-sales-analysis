import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data.csv")

# Preview first few rows
print("\n--- First 5 Rows ---\n")
print(df.head())

# Dataset structure and data types
print("\n--- Dataset Info ---\n")
print(df.info())

# Check for missing values
print("\n--- Missing Values ---\n")
print(df.isnull().sum())

# Convert 'Date' to datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Double check the conversion
print("\n--- Data Types After Date Conversion ---\n")
print(df.dtypes)

# -------------------------
# 1. Monthly Sales Trend
# -------------------------

# Extract month and year from Date
df['Month'] = df['Date'].dt.to_period('M')

# Group total amount by month
monthly_sales = df.groupby('Month')['Total Amount'].sum()

# Display the monthly sales trend
print("\n--- Monthly Sales Trend ---\n")
print(monthly_sales)

# Plot the trend
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind='line', marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# ---------------------------------
# 2. Product Category Performance
# ---------------------------------

# Group data by product category to find total sales and quantity sold
category_sales = df.groupby("Product Category")[["Total Amount", "Quantity"]].sum().sort_values(by="Total Amount", ascending=False)

# Print the results
print("\n--- Product Category Performance ---\n")
print(category_sales)

# Bar chart for Total Sales by Product Category
plt.figure(figsize=(8, 5))
category_sales['Total Amount'].plot(kind='bar', color='teal')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Revenue (₹)')
plt.tight_layout()
plt.show()

# -----------------------------------
# 3. Gender-wise Sales Performance
# -----------------------------------

# Group by Gender and calculate total revenue and quantity
gender_summary = df.groupby("Gender")[["Total Amount", "Quantity"]].sum()
print("\n--- Gender-wise Sales Performance ---\n")
print(gender_summary)

# Bar chart for Gender-based Revenue
plt.figure(figsize=(6, 4))
gender_summary["Total Amount"].plot(kind="bar", color=["purple", "pink"])
plt.title("Total Revenue by Gender")
plt.xlabel("Gender")
plt.ylabel("Revenue (₹)")
plt.tight_layout()
plt.show()

# -------------------------------------------------
# 4. Basket Size Analysis – Overall & Gender-wise
# -------------------------------------------------

# Average basket size (overall)
avg_basket = df['Total Amount'].mean()
print(f"\n--- Average Basket Size (Overall): ₹{avg_basket:.2f} ---")

# Average basket size by gender
basket_by_gender = df.groupby('Gender')['Total Amount'].mean()
print("\n--- Average Basket Size by Gender ---")
print(basket_by_gender)

# Bar chart for average basket size by gender
plt.figure(figsize=(5, 4))
basket_by_gender.plot(kind='bar', color=['orchid', 'steelblue'])
plt.title('Average Basket Size by Gender')
plt.xlabel('Gender')
plt.ylabel('Avg. Spend per Transaction (₹)')
plt.tight_layout()
plt.show()


# -------------------------
# 5. Age Group Analysis
# -------------------------

# Define age bins and labels
bins = [17, 25, 35, 45, 55, 65, 100]
labels = ['18-25', '26-35', '36-45', '46-55', '56-65', '65+']

# Create a new column 'Age Group'
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

# Group by Age Group and calculate total amount and quantity
age_group_sales = df.groupby('Age Group')[['Total Amount', 'Quantity']].sum()

# Display result
print("\n--- Age Group Performance ---\n")
print(age_group_sales)

# Bar chart
plt.figure(figsize=(8, 5))
age_group_sales['Total Amount'].plot(kind='bar', color='purple')
plt.title('Total Sales by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Total Sales Amount')
plt.tight_layout()
plt.show()

# ------------------------------------------
# Monthly Sales Trends by Product Category 
# ------------------------------------------

# Create a 'Month' column (format: YYYY-MM)
df['Month'] = df['Date'].dt.to_period('M')

# Group by Month and Product Category
monthly_category_sales = df.groupby(['Month', 'Product Category'])['Total Amount'].sum().unstack()

# Display trends
print("\n--- Monthly Sales Trend by Category ---\n")
print(monthly_category_sales)

# Plotting the trend
import matplotlib.pyplot as plt

monthly_category_sales.plot(kind='line', marker='o', figsize=(10, 5))
plt.title('Monthly Sales Trend by Product Category')
plt.xlabel('Month')
plt.ylabel('Total Sales (₹)')
plt.legend(title='Product Category')
plt.tight_layout()
plt.show()
