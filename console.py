#!/usr/bin/python3
"""Write a program that contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """class definition of the console"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """exit the program"""
        return True

    def do_EOF(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """do nothing on an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
