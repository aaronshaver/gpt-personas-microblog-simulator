import openai
from io_helper.io_helper import file_to_string
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
        return f"You shall respond using these rules: '{self.get_rules()}'. The setting shall be: '{self.get_setting()}'. The tone of all text should be: '{self.get_tone()}'."

    def get_message(self):
        user_prompt = self.users.get_user_prompt()
        completion = openai.ChatCompletion.create(
            model=global_config.MODEL,
            messages=[
                {"role": "system", "content": self.get_system_content()},
                {"role": "user", "content": user_prompt}
            ]
        )
        message = completion.choices[0].message.content

        data =json.loads(user_prompt)

        conn = sqlite3.connect(global_config.DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (user_name, message) VALUES (?, ?)", (data['user_name'], message))
        conn.commit()
        cursor.execute("SELECT * FROM messages ORDER BY timestamp DESC")
        print('------------------------------------------------')
        for row in cursor.fetchall():
            print(row)
        print('------------------------------------------------')

        return message
