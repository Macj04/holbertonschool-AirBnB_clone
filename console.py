#!/usr/bin/python3
"""Console module for the AirBnB project"""
import cmd
import json
import sys
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """New instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            model_class = eval(arg)
            instance = model_class()
            instance.save()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print string representation"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        try:
            my_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = class_name + '.' + instance_id
        storage.reload()
        instances = storage.all()
        if instance_key in instances:
            print(instances[instance_key])
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation"""
        instances = storage.all()

        if arg:
            try:
                model_class = eval(arg)
                instances = {k: v for k, v in instances.items() if isinstance(v, model_class)}
            except NameError:
                print("** class doesn't exist **")
                return

        print([str(instance) for instance in instances.values()])

    def do_destroy(self, arg):
        """Deletes an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        try:
            model_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = class_name + '.' + instance_id
        storage.reload()
        instances = storage.all()
        if instance_key in instances:
            instances.pop(instance_key)
            storage.save()
        else:
            print("** no instance found **")

    def do_update(self, arg):
        """Updates an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        try:
            model_class = eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        attribute_name = args[2]

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        instance_key = class_name + '.' + instance_id
        instances = storage.all()
        if instance_key not in instances:
            print("** no instance found **")
            return
        instance = instances[instance_key]
        if hasattr(instance, attribute_name):
            attribute_value = type(getattr(instance, attribute_name))(attribute_value)
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        else:
            print("** attribute doesn't exist **")

    def do_quit(self, arg):
        """Quit the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Quit the command interpreter using EOF (Ctrl-D)"""
        print()
        return True

    def do_exit(self, arg):
        """Quit the command interpreter"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
