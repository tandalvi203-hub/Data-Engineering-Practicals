import re

text = "Data Engineering is useful. Data Science is interesting."

# Search
search = re.search("Engineering", text)
print("Search Result:", search.group())

# Split
words = re.split(" ", text)
print("\nSplit Result:", words)

# Replace
new_text = re.sub("Data", "Big Data", text)
print("\nReplaced Text:", new_text)