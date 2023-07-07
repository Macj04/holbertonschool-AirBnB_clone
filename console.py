#!/usr/bin/python3
"""command line interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """To exit the program with Ctrl+C or EOF"""
        return True

    def emptyline(self):
        """An empty line if no input"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
