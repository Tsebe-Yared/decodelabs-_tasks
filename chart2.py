import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned Dataset for Data Analytics.xlsx")

# Chart: Average TotalPrice by Product
df.groupby('Product')['TotalPrice'].mean().sort_values().plot(kind='barh', title='Average Order Value by Product', color='seagreen')
plt.xlabel('Average Total Price ($)')
plt.tight_layout()
plt.savefig('chart_avg_price_by_product.png')
plt.show()