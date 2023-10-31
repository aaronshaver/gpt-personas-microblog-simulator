import openai
from io_helper.io_helper import read_file
import os
from enum import Enum


class Model(Enum):
    GPT_4 = "gpt-4"  # more expensive but more capable
    GPT_35_TURBO = "gpt-3.5-turbo"  # cheap but comparatively dumb


openai.api_key = os.getenv("OPENAI_API_KEY")


class Worker:
    def __init__(self):
        pass

    def get_setting(self, path=None):
        if path is None:
            path = "./world/setting.txt"
        return read_file(path)

    def get_rules(self, path=None):
        if path is None:
            path = "./world/rules.txt"
        return read_file(path)

    def get_system_content(self):
        return f"You shall respond per the following rules: '{self.get_rules()}'. The setting shall be: '{self.get_setting()}' The tone of all the text in all the responses should be: ''."

    def get_user_content(self):
        return """
    {
    "current_user": "DanBalstrud",
    "current_user_persona": "Dan is a 70 year old retired chef; he lives with his younger brother Harry;",
    "recent_messages": []
    }
    """

    def get_message(self):
        completion = openai.ChatCompletion.create(
            model=Model.GPT_35_TURBO.value,
            messages=[
                {"role": "system",
                 "content": self.get_system_content()},
                {"role": "user", "content": self.get_user_content()}
            ]
        )
        return completion.choices[0].message
