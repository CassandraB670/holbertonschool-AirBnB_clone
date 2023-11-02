#!/usr/bin/python3
"""Write a program that contains the entry point of the command interpreter"""
import cmd
import models


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

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it"""
        if not arg:
            print("** class name missing **")
        elif arg not in models.classes:
            print("** class doesn't exist **")
        else:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance
        based on class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.all():
                print(models.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance base on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.all():
                models.all().pop(key)
                models.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name"""
        args = arg.split()
        obj_list = []
        if not arg:
            obj_list = list(models.all().values())
        elif args[0] in models.classes:
            obj_list = [str(obj) for key, obj in models.all().items()
                        if key.split('.')[0] == args[0]]
        else:
            print("** class doesn't exist **")

        for obj_str in obj_list:
            print(obj_str)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = args[0] + "." + args[1]
            if key in models.all():
                instance = models.all()[key]
                attr_name = args[2]
                attr_value = args[3]
                setattr(instance, attr_name, attr_value)
                instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
