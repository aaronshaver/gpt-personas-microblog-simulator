from worker.worker import Worker


if __name__ == "__main__":
    worker = Worker()
    print(worker.get_message())