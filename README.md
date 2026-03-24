# 🛒 E-Commerce Sales Analyzer

## Overview
An end-to-end data analysis project exploring 89,000+ e-commerce orders across 5 related tables using PostgreSQL and Python. The project demonstrates real-world SQL skills including joins, subqueries, and CTEs, alongside Python-based data cleaning, analysis, and visualization.

## Tools Used
- PostgreSQL — data storage and multi-table querying
- Python (pandas, matplotlib, plotly, sklearn) — analysis and visualization
- SQLAlchemy — database connection
- Git & GitHub — version control

## Dataset
- 89,316 records across 5 tables: Customers, Orders, Order Items, Products, Payments
- Source: Kaggle — E-Commerce Order Dataset
- Covers: order status, payment methods, product categories, delivery times, revenue trends

## SQL Concepts Covered
- GROUP BY, COUNT, SUM, AVG, ROUND
- INNER JOIN and LEFT JOIN
- 3-table JOIN (Customers + Orders + Order Items)
- Subquery — customers above average spending
- CTE — monthly revenue trend

## Key Findings
- 97.9% of all orders were successfully delivered
- Credit card is the dominant payment method (73.7% of orders)
- Sao Paulo accounts for 16% of all customers — highest of any city
- November 2017 saw a massive revenue spike — likely Black Friday effect
- Voucher payments had the highest average value ($310) despite low usage
- Product weight has no correlation with price (R²=0.0) — pricing is category driven

## Visualizations
![Orders by Status](chart1_order_status.png)
![Top 10 Categories by Revenue](chart2_category_revenue.png)
![Payment Method Breakdown](chart3_payment_methods.png)
![Monthly Revenue Trend](chart4_monthly_revenue.png)
![Weight vs Price Scatter](chart5_weight_vs_price.png)
![Linear Regression - Weight vs Price](chart6_linear_regression.png)

## How to Run
1. Clone the repo
2. Create a `.env` file with your `DB_PASSWORD`
3. Run `load_data.py` to load all 5 tables into PostgreSQL
4. Run `analysis.py` to generate all charts

> Note: chart5 is an interactive plotly chart — open `chart5_weight_vs_price.html` in your browser for the full interactive experience