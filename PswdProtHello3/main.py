#!/usr/bin/python3
"""An improved version of PswdProtHello2 that can handle an entire list of
possible users.
"""


# Classes
# ===============================================================================
class User(object):
    """A user."""

    def __init__(self, name, pswd):
        """Setup this user."""
        self.name = name
        self.pswd = pswd

    def __eq__(self, user):
        """Compare this user to the given user."""
        return self.name == user.name and self.pswd == user.pswd

    def say_hello(self):
        """Say hello to this user."""
        print("Hello {}!".format(self.name))


class App(object):
    """A basic app."""

    def login(self, name, pswd):
        """Log in using the given username and password."""
        # Create current user
        current_user = User(name, pswd)

        # See if the current user matches any of the users in the list of
        # authorized users.
        for user in self.users:
            if current_user == user:
                return current_user

        # No users matched
        return None

    def run(self):
        """Run this app."""
        # Create list of authorized users and get the current user
        self.users = [
            User("Dylan", "cheetah"),
            User("Fiona", "fox"),
            User("Daniel", "lion"),
            User("Leila", "lioness"),
            User("Abby", "cheetah")
        ]
        current_user = self.login(input("Name: "), input("Pswd: "))

        # Attempt to log in
        if current_user is not None:
            current_user.say_hello()

        else:
            print("***Access Denied***")


# Entry Point
# ===============================================================================
App().run()
