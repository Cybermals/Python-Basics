"""A simple login system."""

import json


#Classes
#===============================================================================
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


class LoginSys(object):
    """A simple login system."""
    def __init__(self):
        """Setup this login system."""
        #Load the user data
        print("Loading user data...", end = "")

        with open("users.json", "r") as f:
            user_data = json.load(f)

        self.users = []

        for user in user_data:
            self.users.append(User(user["name"], user["pswd"]))

        print("ok")

    def login(self, name, pswd):
        """Log in using the given username and password."""
        #Create current user
        current_user = User(name, pswd)

        #See if the current user matches any of the users in the list of
        #authorized users.
        for user in self.users:
            if current_user == user:
                return current_user

        #No users matched
        return None