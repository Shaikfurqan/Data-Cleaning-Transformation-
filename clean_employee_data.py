import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv('../data/raw_employee_data.csv')

# Strip whitespace and standardize name case
df['Name'] = df['Name'].str.strip().str.title()

# Convert 'Age' to numeric, coercing errors to NaN
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# Parse dates in 'JoinDate' column
df['JoinDate'] = pd.to_datetime(df['JoinDate'], errors='coerce')

# Clean 'Salary' and convert to numeric
df['Salary'] = df['Salary'].replace({'\$': '', 'K': '000'}, regex=True)
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Handle missing values
df = df.dropna()

# Save cleaned data
df.to_csv('../data/cleaned_employee_data.csv', index=False)
print("Data cleaned and saved.")
