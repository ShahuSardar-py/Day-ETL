import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "db" / "life.db"
SCHEMA_PATH = BASE_DIR / "schema" / "schema.sql"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    with open(SCHEMA_PATH, "r") as f:
        sql = f.read()

    cursor.executescript(sql)
    conn.commit()
    conn.close()

    print("Database created successfully")

if __name__ == "__main__":
    init_db()
