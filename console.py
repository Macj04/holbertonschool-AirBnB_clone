#!/usr/bin/python3
"""Console module for the AirBnB project"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""
    __clases = {
        "BaseModel": BaseModel,
        "User": User,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

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
        except Exception:
            print("** class is missing **")

    def do_show(self, arg):
        """Print string representation"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in HBNBCommand.__clases:
            print("** class doesn't exist **")
            return
        else:
            my_class = eval(class_name)
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
            if arg not in HBNBCommand.__clases:
                print("** class doesn't exist **")
                return
            else:
                model_class = eval(arg)
                new_instances = {}
            for k, v in instances.items():
                if isinstance(v, model_class):
                    new_instances[k] = v

        print([str(instance) for instance in instances.values()])

    def do_destroy(self, arg):
        """Deletes an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in HBNBCommand.__clases:
            print("** class doesn't exist **")
            return
        else:
            model_class = eval(class_name)
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

        if arg not in HBNBCommand.__clases:
            print("** class doesn't exist **")
            return
        else:
            model_class = eval(class_name)
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
            attr = getattr(instance, attribute_name)
            attribute_value = type(attr)(attribute_value)
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
