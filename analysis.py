import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("DB_PASSWORD")

engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/Ecommerce_analyzer")


# Load all 5 tables
customers = pd.read_sql("SELECT * FROM customers", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)
order_items = pd.read_sql("SELECT * FROM order_items", engine)
products = pd.read_sql("SELECT * FROM products", engine)
payments = pd.read_sql("SELECT * FROM payments", engine)

# Quick overview
print("Customers:", customers.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
print("Products:", products.shape)
print("Payments:", payments.shape)

# Check for nulls in each table
print("\n--- NULLS ---")
print("Customers nulls:\n", customers.isnull().sum())
print("\nOrders nulls:\n", orders.isnull().sum())
print("\nProducts nulls:\n", products.isnull().sum())
print("\nPayments nulls:\n", payments.isnull().sum())

# --- DATA CLEANING ---

# Fill null product categories with 'unknown'
products['product_category_name'] = products['product_category_name'].fillna('unknown')

# Convert date columns to datetime
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_timestamp'] = pd.to_datetime(orders['order_delivered_timestamp'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

# Extract month and year from purchase date
orders['year'] = orders['order_purchase_timestamp'].dt.year
orders['month'] = orders['order_purchase_timestamp'].dt.month

print("✅ Data cleaned!")
print(orders[['order_purchase_timestamp', 'year', 'month']].head())

# --- REGEX CLEANING ---
# Clean product category names - replace underscores with spaces and title case
products['product_category_name'] = products['product_category_name'].str.replace('_', ' ', regex=True).str.title()

print("Sample cleaned categories:")
print(products['product_category_name'].unique()[:10])

# # --- CHART 1: Orders by Status ---
# status_counts = orders['order_status'].value_counts()

# plt.figure(figsize=(10, 6))
# plt.bar(status_counts.index, status_counts.values, color='teal')
# plt.title('Orders by Status')
# plt.xlabel('Order Status')
# plt.ylabel('Number of Orders')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.savefig('chart1_order_status.png')
# plt.show()
# print("✅ Chart 1 saved!")

# # --- CHART 2: Top 10 Product Categories by Revenue (Horizontal Bar) ---
# merged = order_items.merge(products, on='product_id')
# category_revenue = merged.groupby('product_category_name')['price'].sum().sort_values(ascending=False).head(10).sort_values(ascending=True)

# plt.figure(figsize=(10, 6))
# plt.barh(category_revenue.index, category_revenue.values, color='coral')
# plt.title('Top 10 Product Categories by Revenue')
# plt.xlabel('Total Revenue')
# plt.ylabel('Category')
# plt.tight_layout()
# plt.savefig('chart2_category_revenue.png')
# plt.show()
# print("✅ Chart 2 saved!")

# # --- CHART 3: Payment Method Breakdown (Pie Chart) ---
# payment_counts = payments['payment_type'].value_counts()

# plt.figure(figsize=(8, 8))
# plt.pie(payment_counts.values, labels=payment_counts.index, autopct='%1.1f%%', colors=['cyan', 'salmon', 'maroon', 'gold'])
# plt.title('Payment Method Breakdown')
# plt.tight_layout()
# plt.savefig('chart3_payment_methods.png')
# plt.show()
# print("✅ Chart 3 saved!")

# # --- CHART 4: Monthly Revenue Trend (Line Chart) ---
# orders_items_merged = orders.merge(order_items, on='order_id')
# monthly_revenue = orders_items_merged.groupby(['year', 'month'])['price'].sum().reset_index()
# monthly_revenue['date'] = pd.to_datetime(monthly_revenue[['year', 'month']].assign(day=1))
# monthly_revenue = monthly_revenue.sort_values('date')

# plt.figure(figsize=(12, 6))
# plt.plot(monthly_revenue['date'], monthly_revenue['price'], color='indigo', marker='o', linewidth=2)
# plt.title('Monthly Revenue Trend (2016-2018)')
# plt.xlabel('Month')
# plt.ylabel('Total Revenue')
# plt.xticks(rotation=45, ha='right')
# plt.tight_layout()
# plt.savefig('chart4_monthly_revenue.png')
# plt.show()
# print("✅ Chart 4 saved!")

# --- CHART 5: Product Weight vs Price (Interactive Scatter Plot) ---
import plotly.express as px

merged_scatter = order_items.merge(products, on='product_id')
merged_scatter = merged_scatter[merged_scatter['product_weight_g'] < 10000]  # Remove outliers
merged_scatter = merged_scatter.sample(5000, random_state=42) # Reduce the number of points for better performance

fig = px.scatter(
    merged_scatter,
    x='product_weight_g',
    y='price',
    color='product_category_name',
    title='Product Weight vs Price by Category',
    labels={'product_weight_g': 'Product Weight (g)', 'price': 'Price'},
    opacity=0.5 
)

fig.write_html('chart5_weight_vs_price.html')
fig.show()
print("✅ Chart 5 saved!")

# --- LINEAR REGRESSION: Does weight predict price? ---
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

# Prepare data - drop nulls
lr_data = merged_scatter[['product_weight_g', 'price']].dropna()
X = lr_data[['product_weight_g']]
y = lr_data['price']

# Train model
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

# R^2 score
r2 = r2_score(y, y_pred)
print(f"R² Score: {round(r2, 4)}")
print(f"Coefficient: {round(model.coef_[0], 4)}")

# Plot scatter + regression line
plt.figure(figsize=(10, 6))
plt.scatter(lr_data['product_weight_g'], lr_data['price'], alpha=0.3, color='steelblue', s=10, label='Actual')
plt.plot(lr_data['product_weight_g'].sort_values(), 
         model.predict(lr_data[['product_weight_g']].sort_values(by='product_weight_g')), 
         color='red', linewidth=2, label='Regression Line')
plt.title(f'Product Weight vs Price — Linear Regression (R²={round(r2, 4)})')
plt.xlabel('Product Weight (g)')
plt.ylabel('Price')
plt.legend()
plt.tight_layout()
plt.savefig('chart6_linear_regression.png')
plt.show()
print("✅ Chart 6 saved!")