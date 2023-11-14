from flask import Flask, render_template
import sqlite3
from shared import global_config
import hashlib

app = Flask(__name__)


def string_to_html_color(s):
    # Use a hash function to convert the username to a consistent hash.
    hash_object = hashlib.md5(s.encode())
    # Take the first 6 characters of the hash to use as a color.
    hex_color = '#' + hash_object.hexdigest()[:6]
    return hex_color


@app.route('/')
def index():
    conn = sqlite3.connect(global_config.DB_NAME)
    cursor = conn.cursor()

    # fetch messages from the database
    cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC")
    messages = [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
    conn.close()

    # add a consistent hash HTML color for each username in list of messages
    for message in messages:
        message['user_name_color'] = string_to_html_color(message['user_name'])

    # render the template and return
    return render_template('messages.html', messages=messages)
