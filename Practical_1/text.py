import re

with open("sample.txt", "r") as file:
    data = file.read()

print("Extracted Data:")
print(data)

# Find missing values
if re.search(r"Email:\s*$", data, re.MULTILINE):
    print("\nMissing Email: Found")

# Find anomalous age
ages = re.findall(r"Age:\s*(\d+)", data)

for age in ages:
    if int(age) > 100:
        print("Anomalous Age:", age)