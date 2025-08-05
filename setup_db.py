import sqlite3

conn = sqlite3.connect("music.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS music (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    artist TEXT NOT NULL,
    rating REAL NOT NULL
)
""")

# sample music data
cursor.executemany("""
INSERT INTO music (title, artist, rating) VALUES (?, ?, ?)
""", [
    ("Midnight City", "M83", 4.8),
    ("Blinding Lights", "The Weeknd", 4.9),
    ("Random Song", "Unknown Artist", 3.2),
    ("Runaway", "Kanye West", 4.7),
    ("Shape of You", "Ed Sheeran", 4.4),
    ("Dreams", "Fleetwood Mac", 4.6)
])

conn.commit()
conn.close()

print("Database and table created, data inserted.")
