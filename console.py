#!/usr/bin/python3
import cmd

"""command line tool in python"""


class HBNBCommand(cmd.Cmd):
    """make a python command line"""
    prompt = "(hbnb)"

    def emptyline(self):
        """does nothing on empty line"""
        pass

    def do_exit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit program'
        print("")
        return True
