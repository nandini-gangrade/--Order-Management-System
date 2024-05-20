# user.py

class User:
    def __init__(self, userId, username, password, role):
        self.userId = userId
        self.username = username
        self.password = password
        self.role = role

    # Getters
    def get_user_id(self):
        return self.userId

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_role(self):
        return self.role

    # Setters
    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role
