class Users:
    def __init__(self, path=None):
        if path is None:
            path = "./world/users/"

    # this defines the dynamic content that shapes the next new message
    # and includes user name, user background, recent messages (may be empty)
    def get_user_prompt(self):
        return '"user_name": "Bill"'