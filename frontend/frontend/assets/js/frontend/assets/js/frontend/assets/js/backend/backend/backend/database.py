import sqlite3

conn = sqlite3.connect("edupulse.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY,
  name TEXT,
  performance TEXT
)
""")
conn.commit()
