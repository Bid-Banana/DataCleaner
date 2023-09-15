import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('data/customers.csv', delimiter=',')

# Print columns and head for debugging
print("Columns:", df.columns)
print("Head of the DataFrame:")
print(df.head())

# Strip any leading or trailing whitespaces from column names
df.columns = df.columns.str.strip()

# Filter rows where the status is neither active or trialing
remaining_customers = df[~df['Status'].isin(['active', 'trialing'])]


# Save the cleaned DataFrame back to a CSV file
remaining_customers.to_csv('data/remaining_customers.csv', index=False)
