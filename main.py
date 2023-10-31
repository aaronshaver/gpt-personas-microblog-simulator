from worker.worker import Worker
import os


if __name__ == "__main__":
    worker = Worker()

    print(worker.get_message())
    print()
