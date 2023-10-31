import openai
from worker.worker import Worker
import os

openai.api_key = os.getenv("OPENAI_API_KEY")



if __name__ == "__main__":
    worker = Worker()
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": f"You receive standardized input data blocks in JSON form for a simulation of a fictional world. In this world, personas chat with each other on a Twitter-like microblog feed. The setting is as follows: '{worker.get_setting()}'. Your response to the data blocks shall be another piece of valid JSON. You shall output an object with a single key value pair of: a key 'new_message' and a value of a new message. The message shall be in the voice of the current_user persona. To construct the new message, you shall use the user_background supplied in the user prompt as well as content from the recent_messages part of the user prompt. The current_user should be able to respond to others (e.g. '@FooBar that was funny!') but doesn't have to (e.g. 'Today I pet my cat; here's a photo of her' (i.e. a user can simply talk about their own lives without @mention replies to others users. The new_message should be short, similar to messages on a platform like the historic Twitter platform."},
            {"role": "user", "content": worker.user_content}
        ]
    )

    print(completion.choices[0].message)