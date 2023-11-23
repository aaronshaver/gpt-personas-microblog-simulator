from openai import OpenAI
from io_helper.io_helper import file_to_string, minify_string
from shared import global_config
from users.users import Users
import sqlite3
import json


class Worker:
    def __init__(self):
        self.client = OpenAI(api_key=global_config.OPENAI_API_KEY)
        self.users = Users()

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
        s = f"Follow these rules: |{self.get_rules()}| Follow this setting: |{
            self.get_setting()}| Follow this overall tone: |{self.get_tone()}| "
        return minify_string(s)

    # TODO: refactor this function; it's doing way too much and is hard to test
    def produce_message(self):
        """
        forms the system and user content message array which serves as a prompt
        to the OpenAI model; calls the OpenAI API; writes the message the API
        returns to storage along with metadata

        Returns: nothing
        """
        user_prompt = self.users.get_user_prompt()
        s = json.dumps(user_prompt)
        json_string_user_prompt = minify_string(s)

        messages = [
            {"role": "system", "content": self.get_system_content()},
            {"role": "user", "content": json_string_user_prompt}
        ]
        completion = self.client.chat.completions.create(
            model=global_config.MODEL,
            messages=messages
        )

        # prepare message for storage
        message = completion.choices[0].message.content
        message = message[:280]  # enforce a max length

        # write message to storage
        try:
            connection = sqlite3.connect(global_config.DB_NAME)
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO messages (user_name, message, reply_to_user, reply_to_message) VALUES (?, ?, ?, ?)",
                (user_prompt['current_user'], message,
                 user_prompt["reply_to_user"], user_prompt["reply_to_message"])
            )
            connection.commit()
        except Exception as e:
            print(f"Database insert error: {e}")
        finally:
            if 'conn' in locals():
                connection.close()