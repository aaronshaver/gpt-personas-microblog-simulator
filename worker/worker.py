import openai
from io_helper.io_helper import file_to_string
from shared import global_config
from users.users import Users


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
        completion = openai.ChatCompletion.create(
            model=global_config.MODEL,
            messages=[
                {"role": "system", "content": self.get_system_content()},
                {"role": "user", "content": self.users.get_user_prompt()}
            ]
        )
        return completion.choices[0].message
