from worker.worker import Worker
import io_helper.io_helper as io_helper


if __name__ == "__main__":
    io_helper.create_messages_table()

    worker = Worker()

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    for i in range(10):
        print(worker.get_message())
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')