import openai
from io_helper.io_helper import file_to_string, minify_string
from shared import global_config
from users.users import Users
import sqlite3
import json


class Worker:
    def __init__(self):
        self.users = Users()
        openai.api_key = global_config.OPENAI_API_KEY

    def get_setting(self, path=None):
        if path is None:
            path = "./world/setting.txt"
        return file_to_string(path)

    def get_rules(self, path=None):
        if path is None:
            path = "./world/rules.txt"
        return file_to_string(path)

    def get_tone(self, path=None):
        if path is None:
            path = "./world/tone.txt"
        return file_to_string(path)

    def get_system_content(self):
        s = f"Follow these rules: |{self.get_rules()}| Follow this setting: |{self.get_setting()}| Follow this overall tone: |{self.get_tone()}| "
        return minify_string(s)

    def get_message(self):
        # prepare system and user prompts
        user_prompt = self.users.get_user_prompt()
        messages = [
            {"role": "system", "content": self.get_system_content()},
            {"role": "user", "content": user_prompt}
        ]
        completion = openai.ChatCompletion.create(
            model=global_config.MODEL,
            messages=messages
        )

        # prepare data
        data = json.loads(user_prompt)
        message = completion.choices[0].message.content
        message = message[:250]  # enforce a max length

        # write message to database
        conn = sqlite3.connect(global_config.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO messages (user_name, message) VALUES (?, ?)", (data['current_user'], message))
        conn.commit()

        print(f"current_user: {data['current_user']}")
        return message
