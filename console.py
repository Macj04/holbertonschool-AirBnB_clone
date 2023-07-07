#!/usr/bin/python3
"""command line interpreter"""

import cmd

class HBNBCommand(cmd.Cmd):
    """_summary_

    Args:
        cmd (_type_): _description_
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """To exit de program with quit input"""
        return True

    def do_E0F(self, arg):
        """To exit the program with Ctrl+C or EOF"""
        print()
        return True

    def empty_line(self, arg):
        """An empty line if no input"""
        pass

if __name__ == '__main__':
    """Repeatedly issue a prompt, accept input."""
    HBNBCommand().cmdloop()
