#!/usr/bin/python3
"""A command-line user management system."""

import sys

from loginsys import LoginSys, User


# Constants
# ===============================================================================
__version__ = "1.0.0"
header_text = """LoginSys2 v{}
Type 'help' for a list of commands.
""".format(__version__)
help_text = """help - display this message
quit - exit this app
login username, password - log into the system
register username, password - register a new user account
"""


# Classes
# ===============================================================================
class App(object):
    """A basic app class."""

    def __init__(self):
        """Setup this app."""
        self.loginsys = LoginSys()

    def run(self):
        """Run this app."""
        # Print the app header
        print(header_text)

        # Main Loop
        current_user = None

        while True:
            # Get the next command
            cmd = input("cmd> ")

            if " " in cmd:
                cmd, args = cmd.split(" ", 1)
                args = [arg.strip() for arg in args.split(",")]

            else:
                args = []

            # Process the command
            if cmd == "help":
                # Display the help text
                print(help_text)

            elif cmd == "quit":
                # Exit this app
                sys.exit(0)

            elif cmd == "login":
                # Check the command syntax
                if len(args) < 2:
                    print("Syntax Error: 'login' command requires 2 args")

                else:
                    # Login
                    current_user = self.loginsys.login(*args)

                    if current_user is not None:
                        current_user.say_hello()

                    else:
                        print("***Access Denied***")

            elif cmd == "register":
                # Check the command syntax
                if len(args) < 2:
                    print("Syntax Error: 'register' command requires 2 args")

                else:
                    # Register
                    if self.loginsys.register(*args):
                        print("Registration succeeded.")

                    else:
                        print("Registration failed.")

            else:
                # Unknown command
                print("Unknown Command: '{}'".format(cmd))


# Entry Point
# ===============================================================================
if __name__ == "__main__":
    App().run()
