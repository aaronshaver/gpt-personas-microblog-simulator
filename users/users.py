import json
import os
import io_helper.io_helper as io_helper
import random


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
            user_background = io_helper.file_to_string(
                os.path.join(users_dir, file_name))

            user_pairs[user_name] = user_background

        # TODO obviously need to filter out self / current user from this...
        recent_messages = [{"user_name": "Karl2002", "message": "It's been months since we lost contact with Earth. The leaders of this colony won't do anything to try and reconnect."}]

        random_user_name = random.choice(list(user_pairs.keys()))

        data = {
            "user_name": random_user_name,
            "user_background": user_pairs[random_user_name],
            "recent_messages": recent_messages
        }

        return json.dumps(data)
