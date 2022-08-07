#!/usr/bin/python3
import cmd
import sys

"""command line tool in python"""


class CommandLine(cmd.Cmd):
    """make a python command line"""
    intro = 'welcome to the python command line tool. \
            Type help or ? to list commands \n'
    prompt = '(hbnb)'
    file = None

    def do_exit(self, arg):
        'close the command line and exit'
        print('command line has been exit')
        return True

    def do_EOF(self, arg):
        'exit the command line'
        print("you have exit the command line")
        return True


if __name__ == '__main__':
    cm = CommandLine()
    cm.cmdloop()
