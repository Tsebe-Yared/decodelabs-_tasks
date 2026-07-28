import pandas as pd

# Load your already-cleaned dataset
df = pd.read_excel("Cleaned Dataset for Data Analytics.xlsx")

print(df.head())
# Basic statistics for all numeric columns at once
print("\nSummary statistics:")
print(df.describe())
# Find the highest-value orders (potential outliers)
print("\nTop 5 highest TotalPrice orders:")
print(df.nlargest(5, 'TotalPrice')[['OrderID', 'Product', 'Quantity', 'UnitPrice', 'TotalPrice']])
# Average and total sales by product
print("\nAverage TotalPrice by Product:")
print(df.groupby('Product')['TotalPrice'].mean().sort_values(ascending=False))

print("\nOrder count by Product:")
print(df['Product'].value_counts())
# Extract month/year from Date, then look at trends over time
df['Month'] = df['Date'].dt.to_period('M')
print("\nTotal sales by month:")
print(df.groupby('Month')['TotalPrice'].sum())
print("\nOrder count by PaymentMethod:")
print(df['PaymentMethod'].value_counts())

print("\nOrder count by OrderStatus:")
print(df['OrderStatus'].value_counts())