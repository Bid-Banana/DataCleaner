import pandas as pd

# Load the DataFrames
remaining_customers_df = pd.read_csv('data/remaining_customers.csv')
canceled_customers_df = pd.read_csv('data/canceled_customers.csv')

print("Columns of remaining_customers_df:", remaining_customers_df.columns)

# List of canceled customer emails
canceled_emails = canceled_customers_df['Email'].tolist()

# Subtracting canceled customers from the remaining customers to get the abandoned cart customers
abandoned_cart_customers = remaining_customers_df[~remaining_customers_df['Email'].isin(canceled_emails)]

# Save this new list to a new CSV file if desired
abandoned_cart_customers.to_csv('data/abandoned_cart_customers.csv', index=False)
