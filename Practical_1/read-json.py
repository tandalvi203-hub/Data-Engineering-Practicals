import json

# Read JSON file
with open("sample.json", "r") as file:
    data = json.load(file)

print("Extracted Data:")

for student in data["students"]:
    print(student)

# Check missing values
print("\nMissing Values:")

for student in data["students"]:
    for key, value in student.items():
        if value == "":
            print("Missing", key, "for:", student["Name"])

# Check anomalous age
print("\nAnomalous Age:")

for student in data["students"]:
    if student["Age"] > 100:
        print("Anomalous Age:", student["Age"])