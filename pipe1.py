import pandas as pd

# Update these file paths as needed
csv_file_path = 'input.csv'
parquet_file_path = 'output.parquet'

# Load CSV file (assumes there are 5 columns)
df = pd.read_csv(csv_file_path)

# (Optional) Print column names and head to verify
print("Columns:", df.columns)
print(df.head())

# Save DataFrame to Parquet format
df.to_parquet(parquet_file_path, index=False)
print(f"Data saved to {parquet_file_path}")
