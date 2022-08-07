#!/usr/bin/python3
import cmd
import sys

"""command line tool in python"""


class HBNBCommand(cmd.Cmd):
    """make a python command line"""
    prompt = '(hbnb) '

    def do_exit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit program'
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
