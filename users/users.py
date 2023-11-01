import json
import os
import io_helper.io_helper as io_helper

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
        file_names = [f for f in os.listdir(users_dir) if os.path.isfile(os.path.join(users_dir, f))]

        user_pairs = {}
        for file_name in file_names:
            user_name = file_name.split('.')[0]
            user_background = io_helper.file_to_string(os.path.join(users_dir, file_name))

            user_pairs[user_name] = user_background

        recent_messages = ["message1", "message2"]

        for k, v in user_pairs.items():
            user_name = k
            user_background = v

        data = {
            "user_name": user_name,
            "user_background": user_background,
            "recent_messages": recent_messages
        }

        return json.dumps(data)
