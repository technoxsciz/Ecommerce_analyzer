import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
password = os.getenv("DB_PASSWORD")

engine = create_engine(f"postgresql://postgres:{password}@localhost:5432/Ecommerce_analyzer")

# Load all 5 tables
tables = {
    "customers": "csv_files/df_Customers.csv",
    "orders": "csv_files/df_Orders.csv",
    "order_items": "csv_files/df_OrderItems.csv",
    "products": "csv_files/df_Products.csv",
    "payments": "csv_files/df_Payments.csv"
}

for table_name, file_name in tables.items():
    df = pd.read_csv(file_name)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"✅ Loaded {len(df)} rows into '{table_name}'")

print("\n All tables loaded!")