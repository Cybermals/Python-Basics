#!/usr/bin/python3
"""A simple login app."""

from loginsys import LoginSys, User


# Classes
# ===============================================================================
class App(object):
    """A basic app."""

    def __init__(self):
        """Setup this app."""
        self.loginsys = LoginSys()

    def run(self):
        """Run this app."""
        # Log in
        current_user = self.loginsys.login(input("Name: "), input("Pswd: "))

        if current_user is not None:
            current_user.say_hello()

        else:
            print("***Access Denied***")


# Entry Point
# ===============================================================================
if __name__ == "__main__":
    App().run()
