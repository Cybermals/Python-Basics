#!/usr/bin/python3
"""An app that only says hello to an authorized person."""

name = input("Name: ")
pswd = input("Pswd: ")

if name == "Dylan" and pswd == "cheetah":
    print("Hello {}!".format(name))

else:
    print("***Access Denied***")
