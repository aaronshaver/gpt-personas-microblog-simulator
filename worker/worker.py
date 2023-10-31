from io_helper.io_helper import read_file


class Worker:
    def __init__(self):
        pass

    def get_setting(self, path=None):
        if path is None:
            path = "./world/setting.txt"
        return read_file(path)
