from bs4 import BeautifulSoup
import pandas as pd

# Read HTML file
with open("sample.html", "r") as file:
    soup = BeautifulSoup(file, "html.parser")

# Extract table data
table = soup.find("table")
df = pd.read_html(str(table))[0]

print("Extracted Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check anomalous age
print("\nAnomalous Age:")
print(df[df["Age"] > 100])