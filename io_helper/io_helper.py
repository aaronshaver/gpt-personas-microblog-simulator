import re
from shared import global_config
import sqlite3


def file_to_string(path):
    with open(path, 'r') as f:
        return ''.join(f.readlines())


# save tokens (and money) by compressing the system and user prompt text;
# removes string sequences that mostly serve human readers
def minify_string(s):
    s = re.sub(r' +', ' ', s)
    s = re.sub(r'\n+', '\n', s)
    s = re.sub(r'; ', ';', s)
    s = re.sub(r', ', ',', s)
    s = re.sub(r': ', ':', s)
    return s

def create_messages_table():
    connection = sqlite3.connect(global_config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        message TEXT NOT NULL,
        reply_to_user TEXT,
        reply_to_message TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    cursor.execute('''
    CREATE INDEX IF NOT EXISTS idx_timestamp ON messages (timestamp DESC)
    ''')
    connection.commit()
    connection.close()
