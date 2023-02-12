#!/usr/bin/python3
"""This is the console for AirBnB"""
import cmd


class HBNBCommand(cmd.Cmd):
    """this class is entry point of the command interpreter
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Ignores empty spaces"""
        pass

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
