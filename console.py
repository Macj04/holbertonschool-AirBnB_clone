#!/usr/bin/python3
"""command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Command line interpreter for HBNB.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        quit()

    def do_EOF(self, arg):
        """
        Exit the program with Ctrl+D or EOF.
        """
        print()
        quit()

    def emptyline(self):
        """
        An empty line if no input.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
