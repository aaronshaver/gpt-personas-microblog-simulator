from io_helper.io_helper import read_file


class Worker:
    def __init__(self):
        pass

    user_content = """
      {
      "current_user": "DanBlizzard",
      "current_user_persona": "Dan is a 70 year old retired chef; he lives with his younger brother Harry; he is obsessed with VR gaming as a hobby",
      "recent_messages": []
      }
      """

    def get_setting(self, path=None):
        if path is None:
            path = "./world/setting.txt"
        return read_file(path)
