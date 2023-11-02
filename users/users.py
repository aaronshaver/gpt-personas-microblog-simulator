import json
import os
import io_helper.io_helper as io_helper
import random
import sqlite3
from shared import global_config


class Users:
    def __init__(self, path=None):
        self.path = path
        if path is None:
            self.path = "../world/users/"

    # this defines the dynamic content that shapes the next new message
    # and includes user name, user background, recent messages (may be empty)
    def get_user_prompt(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        users_dir = os.path.join(current_dir, self.path)
        file_names = [f for f in os.listdir(
            users_dir) if os.path.isfile(os.path.join(users_dir, f))]

        user_pairs = {}
        for file_name in file_names:
            user_name = file_name.split('.')[0]
            user_background = io_helper.file_to_string(
                os.path.join(users_dir, file_name))

            user_pairs[user_name] = user_background

        random_user_name = random.choice(list(user_pairs.keys()))

        recent_message = self.get_recent_message(random_user_name)

        data = {
            "user_name": random_user_name,
            "user_background": user_pairs[random_user_name],
            "recent_message": recent_message
        }

        s = json.dumps(data)
        return io_helper.minify_string(s)

    def get_recent_message(self, user_name):
        conn = sqlite3.connect(global_config.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM messages WHERE user_name != ? ORDER BY timestamp DESC LIMIT 10", (user_name,))
        messages = []
        for row in cursor.fetchall():
            messages.append(row)
        if not messages:
            return ""
        random_message = random.choice(messages)
        print(random_message)

        return {"user_name": random_message[1], "message": random_message[2]}