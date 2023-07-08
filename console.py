#!/usr/bin/python3
"""Command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """When user use Ctrl+D"""
        return True

    def emptyline(self):
        """New line at empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
