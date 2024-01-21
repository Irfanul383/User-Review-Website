class User:
    user_id: int
    username: str
    password: str
    is_logged_in: int

    def __init__(self, user_id, username, password, is_logged_in=0):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_logged_in = is_logged_in
