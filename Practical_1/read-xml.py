import xml.etree.ElementTree as ET

# Read XML file
tree = ET.parse("sample.xml")
root = tree.getroot()

print("Extracted Data:")

for student in root.findall("student"):
    print(
        student.find("ID").text,
        student.find("Name").text,
        student.find("Age").text,
        student.find("City").text,
        student.find("Email").text
    )

# Check missing values
print("\nMissing Values:")

for student in root.findall("student"):
    if not student.find("Email").text:
        print("Missing Email found for:", student.find("Name").text)

# Check anomalous age
print("\nAnomalous Age:")

for student in root.findall("student"):
    age = int(student.find("Age").text)
    if age > 100:
        print("Anomalous Age:", age)