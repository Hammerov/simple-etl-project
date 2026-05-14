# create_data.py
import pandas as pd

# Create sample sales data (10 rows only)
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'customer_name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 
                      'Frank', 'Grace', 'Henry', 'Ivy', 'Jack'],
    'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Laptop',
                'Mouse', 'Keyboard', 'Monitor', 'Laptop', 'Mouse'],
    'quantity': [1, 2, 1, 1, 1, 3, 2, 1, 1, 2],
    'price': [1000, 25, 75, 300, 1000, 25, 75, 300, 1000, 25],
    'sale_date': ['2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', 
                  '2024-01-03', '2024-01-04', '2024-01-04', '2024-01-05',
                  '2024-01-05', '2024-01-06']
}

df = pd.DataFrame(data)
df.to_csv('data/sales_data.csv', index=False)
print("✅ sales_data.csv created in 'data' folder with 10 rows!")
print(df)