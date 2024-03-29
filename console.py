#!/usr/bin/python3
"""
The console v: 0.0.1
Contains the entry point of the command interpreter
"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """a class that inherits from cmd"""

    prompt = "(hbnb) "
    classNames = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, className):
        """create a new object and save it"""
        if className and className in self.classNames:
            #my_model = BaseModel()
            my_model = eval(className)()
            my_model.save()
            print(my_model.id)
        elif className:
            print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, args):
        """show object based on class name and id"""
        myArgs = args.split(" ")
        my_object = storage.all()
        #print(myArgs)
        #print(len(myArgs))
        if myArgs[0] == "":
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
                    #print(my_object["{}.{}".format(myArgs[0], myArgs[1])])
                    new_obj = my_object["{}.{}".format(myArgs[0], myArgs[1])]
                    individualDict = new_obj.to_dict()
                    print("[{}] ({}) {}".format(new_obj.__class__.__name__, individualDict['id'], individualDict))

    def do_destroy(self, args):
        """show object based on class name and id"""
        myArgs = args.split(" ")
        my_object = storage.all()
        print(myArgs)
        print(len(myArgs))
        if myArgs[0] == "":
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

    def do_all(self, args):
        """print all instances"""
        myArgs = args.split(" ")
        my_object = storage.all()
        if myArgs[0] == "":
            print(my_object)
        elif myArgs[0] not in self.classNames:
            print("** class doesn't exist **")
        else:
            print(my_object)

    def do_update(self, args):
        """update instance given class name, id, key and variable"""
        myArgs = args.split(" ")
        my_object = storage.all()
        print(myArgs)
        print(len(myArgs))
        if myArgs[0] == "":
            print("** class name missing **")
        elif len(myArgs) == 1:
            print("** instance id missing **")
        elif len(myArgs) == 2:
            print("** attribute name missing **")
        elif len(myArgs) == 3:
            print("** value missing **")
        else:
            if myArgs[0] not in self.classNames:
                print("** class doesn't exist **")
            else:
                if "{}.{}".format(myArgs[0], myArgs[1]) not in my_object:
                    print("** no instance found **")
                else:
                    #my_object["{}.{}".format(myArgs[0], myArgs[1])]["{}".format(myArgs[2])] = myArgs[3]
                    setattr(my_object["{}.{}".format(myArgs[0], myArgs[1])], myArgs[2], myArgs[3])
                    storage.save()

    def emptyline(self):
        """action to take on empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
