#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """a class that inherits from cmd"""

    prompt = "(hbnb) "
    classNames = ["BaseModel"]

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, className):
        """create a new object and save it"""
        if className and className in self.classNames:
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        elif className:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def emptyline(self):
        """action to take on empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
