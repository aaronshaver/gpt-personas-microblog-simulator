from flask import Flask, render_template
import sqlite3
from shared import global_config

app = Flask(__name__)


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
