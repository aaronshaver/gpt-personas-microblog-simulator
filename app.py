from flask import Flask, render_template
import sqlite3
from shared import global_config
import os

app = Flask(__name__)


print("absolute path of db:")
print(os.path.abspath(global_config.DB_NAME))
print(f"we're in app.py and web container and will try connecting to database at: {
      global_config.DB_NAME}")


@app.route('/')
def index():
    conn = sqlite3.connect(global_config.DB_NAME)
    cursor = conn.cursor()

    # fetch messages from the database
    cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC")
    messages = [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
    conn.close()

    # render the template and return
    return render_template('messages.html', messages=messages)
