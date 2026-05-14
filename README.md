# 🚀 ETL Pipeline: CSV to PostgreSQL

## 📌 Project Overview
Production-ready ETL pipeline that extracts sales data from CSV files, transforms it with data quality checks, and loads into PostgreSQL for business analytics.

## 🛠️ Tech Stack
- **Python 3.10** - Core ETL logic
- **Pandas** - Data transformation
- **PostgreSQL** - Data warehouse
- **SQLAlchemy** - Database connection
- **Bash** - Automation scripts

## 📊 ETL Process

### Extract
- Reads raw sales data from CSV files
- Handles various data formats

### Transform
- Calculates total_amount (quantity × price)
- Removes duplicate records
- Validates data quality (no negative prices)
- Converts date formats

### Load
- Loads clean data to PostgreSQL
- Maintains data integrity
- Provides loading confirmation

## 📈 Business Insights Generated
- Total revenue analysis
- Top performing products
- Customer spending patterns
- Daily sales trends

## 🚀 Quick Start

### Prerequisites
```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Create database
sudo -u postgres psql -c "CREATE DATABASE sales_db;"