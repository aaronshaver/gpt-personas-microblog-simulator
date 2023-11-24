from enum import Enum
import os


class Model(Enum):
    GPT_4 = "gpt-4"  # more expensive but more capable
    GPT_35_TURBO = "gpt-3.5-turbo"  # cheaper but makes dumb mistakes


# set your preferred OpenAI LLM model
MODEL = Model.GPT_35_TURBO.value

# the percent chance the current user replies to a recent message
REPLY_CHANCE = 0.75

# set this however you like, e.g. via `export OPENAI_API_KEY=<key>` in ~/.zshrc
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if os.getenv('DOCKER_ENV'):
    DB_NAME = '/app/db/database.db'  # path inside Docker
else:
    DB_NAME = 'local_database.db'  # local path for development/testing

MAX_MESSAGES = 100  # "safety valve" so we don't spend tons of OpenAI API money

SECONDS_BETWEEN_MESSAGES = 60

# this is how far back the system will search when looking for a recent message
# to respond to if/when it is attempting to generate a reply response (a user
# at-mentioning another user and replying to the content of their message)
RECENT_REPLIES_DEPTH = 20