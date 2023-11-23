from flask import Flask, render_template, request, redirect, url_for
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
    connection = sqlite3.connect(global_config.DB_NAME)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC")
    # get a list of messages, where each message is a dictionary, and in each
    # dictionary, keys are table column names like 'user_name'
    messages = [dict(zip([column[0] for column in cursor.description], row))
                for row in cursor.fetchall()]
    connection.close()

    # add a consistent hash HTML color for each username in list of messages
    for message in messages:
        message['user_name_color'] = string_to_html_color(message['user_name'])

    # render the template and return
    return render_template('messages.html', messages=messages)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    """
    allows the user to inject a message into the stream (that the bots can later
    reply to); in other words, makes the application interactive

    note: this doesn't support the nice display of replying to a user; but
    that could be easily accomplished by adding an 'id' field in the input
    form and looking up that user+message for writing to reply_to_user and
    reply_to_message
    """
    if request.method == 'POST':
        current_user = request.form['username']
        message = request.form['message']

        connection = sqlite3.connect(global_config.DB_NAME)
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO messages (user_name, message, reply_to_user, reply_to_message) VALUES (?, ?, ?, ?)",
                (current_user, message, '', '')
            )
            connection.commit()
        except Exception as e:
            print(f"Database insert error: {e}")
        finally:
            connection.close()

        return redirect(url_for('admin'))

    return render_template('admin.html')