from worker.worker import Worker
import sqlite3
from shared import global_config


if __name__ == "__main__":
    conn = sqlite3.connect(global_config.DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        message TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

    worker = Worker()
    print(worker.get_message())