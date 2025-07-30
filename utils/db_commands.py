from config import cursor, database_connection, FILE_PATH
import sqlite3

def create_users_table():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            subcategory TEXT,
            city TEXT,
            name TEXT,
            passport TEXT,
            birth_date TEXT,
            passport_validity TEXT,
            gender TEXT,
            phone TEXT,
            nation TEXT,
            book_data_from TEXT,
            book_data_to TEXT,
            candidate_number TEXT,
            registered INTEGER DEFAULT 0,
            booked INTEGER DEFAULT 0,
            email TEXT,
            password TEXT,
            token TEXT
        )
    """)
    database_connection.commit()


def insert_into_table(table_name: str, **row_data):
    """insertion query into specific table"""
    columns = ", ".join(row_data.keys())
    placeholders = ", ".join(["?"] * len(row_data))
    values = tuple(row_data.values())

    command = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(command, values)
    database_connection.commit()


def read_from_table(table_name: str) -> list[tuple]:
    create_users_table()
    """Table read query"""
    command = f"SELECT * FROM {table_name}"
    cursor.execute(command)
    return cursor.fetchall()


def fetch_all_users_as_dict(db_path):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row 
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    result = [dict(row) for row in rows]
    conn.close()
    return result