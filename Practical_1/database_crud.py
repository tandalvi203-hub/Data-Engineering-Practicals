import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# CREATE
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

# INSERT
cursor.execute("INSERT INTO students VALUES (1, 'Rahul', 21, 'Mumbai')")
cursor.execute("INSERT INTO students VALUES (2, 'Priya', 22, 'Pune')")
conn.commit()

# READ
print("Student Records:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

# UPDATE
cursor.execute("UPDATE students SET city='Nashik' WHERE id=2")
conn.commit()

# DELETE
cursor.execute("DELETE FROM students WHERE id=1")
conn.commit()

print("\nRecords after UPDATE and DELETE:")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()