from worker import Worker
from io_helper.io_helper import create_messages_table
from shared import global_config
import time

if __name__ == "__main__":
    create_messages_table()
    worker = Worker()

    for i in range(global_config.MAX_MESSAGES):
        worker.produce_message()
        time.sleep(global_config.SECONDS_BETWEEN_MESSAGES)