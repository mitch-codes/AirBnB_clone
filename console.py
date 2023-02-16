#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """a class that inherits from cmd"""

    intro = "this is my cmd"
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """exit the program"""
        return True
    
    def emptyline(self):
        """action to take on empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
