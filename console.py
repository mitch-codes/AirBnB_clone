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

    def do_show(self, args):
        """show object based on class name and id"""
        tokens = args.split(" ")
        if len(tokens) == 0:
            print("** class name missing **")
            return
        if tokens[0] not in HBNBCommand.my_dict.keys():
            print("** class doesn't exist **")
            return
        if len(tokens) <= 1:
            print("** instance id missing **")
            return
        storage.reload()
        objs_dict = storage.all()
        key = tokens[0] + "." + tokens[1]
        if key in objs_dict:
            obj_instance = str(objs_dict[key])
            print(obj_instance)
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """show object based on class name and id"""
        myArgs = args.split(" ")
        my_object = storage.all()
        print(myArgs)
        print(len(myArgs))
        if len(myArgs) == 0:
            print("** class name missing **")
        elif len(myArgs) == 1:
            print("** instance id missing **")
        else:
            if myArgs[0] not in self.classNames:
                print("** class doesn't exist **")
            else:
                if "{}.{}".format(myArgs[0], myArgs[1]) not in my_object:
                    print("** no instance found **")
                else:
                    del my_object["{}.{}".format(myArgs[0], myArgs[1])]
                    storage.save()

    def emptyline(self):
        """action to take on empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
