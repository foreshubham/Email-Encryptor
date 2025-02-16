import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    masked_email TEXT PRIMARY KEY,
    encrypted_email TEXT
)
""")

conn.commit()
conn.close()

print("Database setup complete.")
