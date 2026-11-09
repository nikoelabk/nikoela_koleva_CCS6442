"""Entry point for running the User example."""

from app.core.user import User

if __name__ == "__main__":
    user1 = User("Maria", "Software developer from Greece")
    print(user1)