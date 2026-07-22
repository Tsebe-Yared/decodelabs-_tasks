import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned Dataset for Data Analytics.xlsx")

df['OrderStatus'].value_counts().plot(kind='bar', title='Order Count by Status', color='steelblue')
plt.ylabel('Number of Orders')
plt.tight_layout()
plt.savefig('chart_order_status.png')
plt.show()