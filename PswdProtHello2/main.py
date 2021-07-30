#!/usr/bin/python3
"""An improved version of PswdProtHello that uses objects."""


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


#Entry Point
#===============================================================================
dylan = User("Dylan", "cheetah")
current_user = User(input("Name: "), input("Pswd: "))

if current_user == dylan:
    current_user.say_hello()

else:
    print("***Access Denied***")
