# Writing to a binary file
data = b"Hello, Data Engineering!"

with open("sample.bin", "wb") as file:
    file.write(data)

print("Data written successfully.")

# Reading from a binary file
with open("sample.bin", "rb") as file:
    data = file.read()

print("Data read from binary file:")
print(data)