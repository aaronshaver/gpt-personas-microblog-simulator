from enum import Enum
import os

# OpenAI model
class Model(Enum):
    GPT_4 = "gpt-4"  # more expensive but more capable
    GPT_35_TURBO = "gpt-3.5-turbo"  # cheaper but makes dumb mistakes
MODEL = Model.GPT_4.value

# percent chance current user replies to recent messages
REPLY_CHANCE = 0.5

# set this however you like, e.g. via `export OPENAI_API_KEY=<key>` in ~/.zshrc
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if os.getenv('DOCKER_ENV'):
    DB_NAME = '/app/db/database.db'  # path inside Docker
else:
    DB_NAME = 'local_database.db'  # local path for development/testing

MAX_MESSAGES = 100
SECONDS_BETWEEN_MESSAGES = 60