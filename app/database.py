import sqlite3
DATABASE_URI = "db/search_sightings.db"

# Create a SQLite database if it doesn't exist already.
def create_tables():
    conn = sqlite3.connect(DATABASE_URI)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ufo_sightings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date_occurred TEXT,
        date_posted TEXT,
        city TEXT,
        state TEXT,
        country TEXT,
        shape TEXT,
        summary TEXT
    )
    ''')

    conn.commit()
    conn.close()

create_tables()
