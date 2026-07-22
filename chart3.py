import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned Dataset for Data Analytics.xlsx")

df['Month'] = df['Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['TotalPrice'].sum()

monthly_sales.plot(kind='line', marker='o', title='Total Sales by Month', color='darkorange', figsize=(10,5))
plt.ylabel('Total Sales ($)')
plt.xlabel('Month')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('chart_sales_by_month.png')
plt.show()