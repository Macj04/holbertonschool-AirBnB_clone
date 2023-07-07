#!/usr/bin/python3
"""command line interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """To exit de program with quit input"""
        return True

    def do_E0F(self, arg):
        """To exit the program with Ctrl+C or EOF"""
        return True

    def empty_line(self, arg):
        """An empty line if no input"""
        cmd.emptyline()

if __name__ == '__main__':
    """Repeatedly issue a prompt, accept input, parse an initial prefix off the received input, and dispatch to action methods, passing them the remainder of the line as argument."""
    HBNBCommand().cmdloop()
