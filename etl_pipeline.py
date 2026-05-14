import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
import os

# Database connection (adjust username if needed)
DATABASE_URL = "postgresql://lk:password@localhost:5432/sales_db"
engine = create_engine(DATABASE_URL)

print("=" * 50)
print("🚀 STARTING ETL PIPELINE")
print("=" * 50)

# STEP 1: EXTRACT
print("\n📂 STEP 1: Extracting data from CSV...")
df = pd.read_csv('sales_data.csv')
print(f"   ✅ Extracted {len(df)} rows")

# STEP 2: TRANSFORM
print("\n🔄 STEP 2: Transforming data...")

# Calculate total amount
df['total_amount'] = df['quantity'] * df['price']
print(f"   ✅ Added 'total_amount' column")

# Data quality checks
if (df['price'] < 0).any():
    print("   ⚠️  Warning: Negative prices found")
else:
    print("   ✅ No negative prices found")

# Remove duplicates
df = df.drop_duplicates(subset=['order_id'])
print(f"   ✅ After deduplication: {len(df)} rows")

# Convert date
df['sale_date'] = pd.to_datetime(df['sale_date'])

print(f"   📊 Final dataset: {len(df)} rows")

# STEP 3: LOAD
print("\n💾 STEP 3: Loading to PostgreSQL...")
try:
    df.to_sql('sales', engine, if_exists='replace', index=False)
    print(f"   ✅ Loaded {len(df)} rows into 'sales' table")
except Exception as e:
    print(f"   ❌ Database error: {e}")
    print("   Make sure PostgreSQL is running: sudo systemctl start postgresql")
    exit(1)

# STEP 4: VERIFY
print("\n📊 VERIFICATION: Reading back from database...")
result = pd.read_sql("SELECT COUNT(*) as count FROM sales", engine)
count = result['count'][0]
print(f"   ✅ Verified: {count} rows in database")

# Business insights
print("\n📈 BUSINESS INSIGHTS:")
revenue = pd.read_sql("SELECT SUM(total_amount) as total FROM sales", engine)
print(f"   💰 Total Revenue: ${revenue['total'][0]:,.2f}")

top_product = pd.read_sql("""
    SELECT product, SUM(total_amount) as revenue 
    FROM sales 
    GROUP BY product 
    ORDER BY revenue DESC 
    LIMIT 1
""", engine)
print(f"   🏆 Top Product: {top_product['product'][0]} (${top_product['revenue'][0]:,.2f})")

print("\n" + "=" * 50)
print(f"✅ ETL COMPLETED at {datetime.now()}")
print("=" * 50)
