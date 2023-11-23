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
    # and includes user name, user background, recent message info (which may be
    # empty)
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
            "current_user": random_user_name,
            "current_user_background": user_pairs[random_user_name],
            "reply_to_user": "" if not recent_message else recent_message["reply_to_user"],
            "reply_to_message": "" if not recent_message else recent_message["reply_to_message"],
        }
        return data

    def should_not_reply(self):
        """
        do not return a message if we are over the reply_chance threshold
        example: if random number is 0.8555, and our reply_chance is 0.2, we
        don't do a reply; so only values 0 to 0.1999... will initiate reply
        """
        if random.random() > global_config.REPLY_CHANCE:
            return True

    def get_recent_message(self, user_name):
        """
        grabs a recent message from storage that does not match the current (i.e.
        speaking) user so that current user can potentially reply to it

        user_name (string): the current user about to post a message

        Returns:
        JSON string if message available, or empty string otherwise
        """
        if self.should_not_reply():
            return ""

        messages = []
        try:
            connection = sqlite3.connect(global_config.DB_NAME)
            cursor = connection.cursor()
            cursor.execute(
                "SELECT * FROM messages WHERE user_name != ? ORDER BY timestamp DESC LIMIT 20", (user_name,))
            for row in cursor.fetchall():
                messages.append(row)
            if not messages:
                return ""
        except Exception as e:
            print(f"Database select error: {e}")
        finally:
            if 'conn' in locals():
                connection.close()

        random_message = random.choice(messages)

        return {"reply_to_user": random_message[1], "reply_to_message": random_message[2]}