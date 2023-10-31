import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


class Worker:
    def __init__(self):
        pass

    user_content = """
      {
      "fictional_setting": "The tone of the fictional text should be dark and gritty like a cyberpunk story (but not overly bleak or crude or violent); Earth; 2050; a society struggling with severe climate change; but also benefiting from advanced technology like ultra-realistic virtual reality, commonplace driverless cars, and the early stages of a human-inhabited Mars colony;",
      "current_poster": "DanBlizzard",
      "current_poster_persona": "Dan is a 70 year old retired chef; he lives with his younger brother Harry; he is obsessed with VR gaming as a hobby, but he also maintains a small garden on his high-rise patio",
      "recent_messages": [{"message_id": 2, "poster_name": "AaronShaver", "message": "@DanBlizzard Ultimate Thunder's haptics are next level, man! Try my VR detox routine so you don't become a sleep-deprived zombie. #VRlife"}, {"message_id": 1, "poster_name": "DanBlizzard", "message": "I can't stop playing Ultimate Thunder! The haptics are incredible and I've already made a few friends but it's eating into my sleep, haha"}]
      }
      """

    def get_setting(self, path=None):
        if path is None:
            path = "./world/setting.txt"
        output = ""
        with open(path, 'r') as f:
            output = ''.join(f.readlines())
        return output

    # completion = openai.ChatCompletion.create(
    #     model="gpt-4",
    #     messages=[
    #         {"role": "system",
    #          "content": "You receive standardized input data blocks for a fun simulation of a fictional world where fictional personas chat with each other on a Twitter-like microblog feed. Your response to the data blocks should be another piece of valid JSON text. The required fields you will output shall be a JSON object with key value pairs of: a key 'new_message' and a value of a new message from the current_poster persona. You will use the fictional setting supplied, as well as the current poster's persona description, as well as recent messages to generate the new_message. The current_poster should be able to respond to others (e.g. '@FooBar that was funny!') but doesn't have to, and can just talk about their own things too. The new_message should be short, pithy, and punchy, similar to messages on a Twitter-like microblog feed. Try not to exceed 140 characters."},
    #         {"role": "user", "content": user_content}
    #     ]
    # )

    # print(completion.choices[0].message)