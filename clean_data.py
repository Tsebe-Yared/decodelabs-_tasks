import pandas as pd

# Load the Excel file into a table (called a "DataFrame")
df = pd.read_excel("Dataset for Data Analytics.xlsx")

# Show the first 5 rows just to see what we're working with
print(df.head())
# Check how many missing values are in each column
print("\nMissing values per column:")
print(df.isnull().sum())
# Fill missing CouponCode values with a clear label
df['CouponCode'] = df['CouponCode'].fillna('No Coupon')

# Confirm it worked - this should now show 0 missing
print("\nMissing values after fixing CouponCode:")
print(df.isnull().sum())
# Check for duplicate rows
print("\nNumber of duplicate rows:", df.duplicated().sum())
# Check what data type each column currently has
print("\nData types of each column:")
print(df.dtypes)
# Look at unique values in key text columns to spot inconsistencies
print("\nUnique Products:", df['Product'].unique())
print("\nUnique PaymentMethods:", df['PaymentMethod'].unique())
print("\nUnique OrderStatus:", df['OrderStatus'].unique())
# Double-check for extra spaces hiding in text columns
print("\nChecking for leading/trailing spaces in ShippingAddress:")
print(df['ShippingAddress'].str.strip().equals(df['ShippingAddress']))

# Double-check Quantity and ItemsInCart aren't negative or zero (which wouldn't make sense)
print("\nAny negative or zero Quantity?", (df['Quantity'] <= 0).any())
print("Any negative or zero ItemsInCart?", (df['ItemsInCart'] <= 0).any())
df.to_excel("Cleaned_Dataset_for_Data_Analytics.xlsx", index=False)
print("\nCleaned file saved successfully!")