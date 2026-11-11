class User:
    """Plain user class used for the Git workflow exercises."""
    def __init__(self, username, the_bio):
        self.username = username
        self.bio = the_bio

    def get_username(self):
        return self.username

    def set_username(self, the_name):
        self.username = the_name

        def __str__(self):
           return f"name: {self.username}, bio: {self.bio}"
