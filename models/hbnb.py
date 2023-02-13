#!/usr/bin/python3
""" Implementation of the interpretor """


import cmd


class Hbnb(cmd.Cmd):
    """ the interprator module """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Provides a proper exit to the interpreter """
        return True

    def do_EOF(self, line):
        """ Provides a proper exit with other options """
        return True

    def emptyline(self):
        """Overrides the parent class method"""
