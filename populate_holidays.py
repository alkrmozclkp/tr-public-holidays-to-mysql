import mysql.connector
from holidays import Turkey
from datetime import date

# Database configuration
DB_CONFIG = {
    'host': '127.0.0.1',
    'port': 8080,
    'user': 'root',
    'password': 'kerem',
    'database': 'tr_public_holidays'
}

TABLE_NAME = 'public_holidays'

def create_table(cursor):
    """Creates the table if it does not exist."""
    query = f"""
    CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
        id INT AUTO_INCREMENT PRIMARY KEY,
        holiday_date DATE NOT NULL,
        holiday_name VARCHAR(255) NOT NULL,
        UNIQUE (holiday_date, holiday_name)
    );
    """
    try:
        cursor.execute(query)
        print(f"Table '{TABLE_NAME}' created or already exists.")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

def insert_holiday(cursor, holiday_date, holiday_name):
    """Inserts a holiday into the database (avoids duplicates)."""
    query_insert = f"""
    INSERT INTO {TABLE_NAME} (holiday_date, holiday_name)
    VALUES (%s, %s)
    ON DUPLICATE KEY UPDATE holiday_date = VALUES(holiday_date);
    """
    try:
        cursor.execute(query_insert, (holiday_date, holiday_name))
        print(f"Inserted: {holiday_date} - {holiday_name}")
    except mysql.connector.Error as err:
        print(f"Error inserting ({holiday_date} - {holiday_name}): {err}")

def main():
    try:
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()

        create_table(cursor)

        current_year = date.today().year
        for year in range(current_year, current_year + 10):
            print(f"\n--- Fetching holidays for {year} ---")
            tr_holidays = Turkey(years=year)
            for holiday_date, holiday_name in sorted(tr_holidays.items()):
                insert_holiday(cursor, holiday_date, holiday_name)

        db.commit()
        print("\n All holidays have been inserted into the database.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'db' in locals():
            db.close()
            print(" Database connection closed.")

if __name__ == "__main__":
    main()
