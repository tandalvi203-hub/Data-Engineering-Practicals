import pandas as pd
from sqlalchemy import create_engine

# ==============================
# 1. EXTRACT - CSV FILES
# ==============================

df1 = pd.read_csv("customers1.csv")
df2 = pd.read_csv("customers2.csv")

# Combine multiple CSV files
csv_data = pd.concat([df1, df2], ignore_index=True)

print("\nCombined CSV Data:")
print(csv_data)


# ==============================
# 2. EXTRACT - JSON FILE
# ==============================

json_data = pd.read_json("customers.json")

print("\nJSON Data:")
print(json_data)


# ==============================
# 3. TRANSFORM
# ==============================

# Combine CSV and JSON data
data = pd.concat([csv_data, json_data], ignore_index=True)

# Remove duplicate records
data = data.drop_duplicates()

# Convert data types
data["age"] = pd.to_numeric(data["age"], errors="coerce")
data["salary"] = pd.to_numeric(data["salary"], errors="coerce")

# ==============================
# 4. REMOVE INVALID RECORDS
# ==============================

# Remove records with missing values
data = data.dropna()

# Remove invalid ages
data = data[(data["age"] > 0) & (data["age"] < 100)]

# Remove invalid salaries
data = data[data["salary"] > 0]

print("\nCleaned Data:")
print(data)


# ==============================
# 5. DATA VALIDATION
# ==============================

required_columns = ["id", "name", "age", "city", "salary"]

if all(column in data.columns for column in required_columns):
    print("\nData Validation: PASSED")
else:
    print("\nData Validation: FAILED")
    exit()


# ==============================
# 6. DATA TRANSFORMATION
# ==============================

# Create salary category
data["salary_category"] = data["salary"].apply(
    lambda x: "High" if x >= 60000 else "Medium" if x >= 45000 else "Low"
)

print("\nTransformed Data:")
print(data)


# ==============================
# 7. LOAD INTO DATABASE
# ==============================

engine = create_engine("sqlite:///etl_database.db")

data.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("\nData successfully loaded into SQLite database.")


# ==============================
# 8. VERIFY DATABASE
# ==============================

loaded_data = pd.read_sql("SELECT * FROM customers", engine)

print("\nData stored in database:")
print(loaded_data)

print("\nETL Pipeline completed successfully!")