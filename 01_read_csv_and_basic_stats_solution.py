# Solution to Exercise 01: Read CSV and Basic Stats

import pandas as pd

# 1. Load the dataset
df = pd.read_csv('data.csv')

# 2. Print the first five rows
print("First 5 rows:")
print(df.head())

# 3. Show DataFrame structure
print("\nDataFrame info:")
print(df.info())

# 4. Summary statistics
print("\nSummary statistics:")
print(df.describe())

# 5. Missing values in each column
print("\nMissing values per column:")
print(df.isnull().sum())
