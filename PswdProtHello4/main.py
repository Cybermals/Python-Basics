#!/usr/bin/python3
"""An improved version of PswdProtHello3 that reads a list of users from a file.
"""


#Classes
#===============================================================================
class User(object):
    """A user."""
    @staticmethod
    def load_from_file(f):
        """Load a user from a config file."""
        name = f.readline().split("=")[1].strip()
        pswd = f.readline().split("=")[1].strip()
        return User(name, pswd)

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
    def __init__(self):
        """Setup this app."""
        #Load the list of authorized users
        print("Loading user list...", end = "")
        self.users = []

        with open("users.cfg", "r") as f:
            for line in f:
                if line.strip() == "[User]":
                    self.users.append(User.load_from_file(f))

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

    def run(self):
        """Run this app."""
        #Get the current user
        current_user = self.login(input("Name: "), input("Pswd: "))

        #Attempt to log in
        if current_user is not None:
            current_user.say_hello()

        else:
            print("***Access Denied***")


#Entry Point
#===============================================================================
App().run()
