import pandas as pd

# Read CSV file
df = pd.read_csv("sample.csv")

print("Extracted Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check anomalous age
print("\nAnomalous Age:")
print(df[df["Age"] > 100])