#!/usr/bin/python3
""" Implementation of the interpretor """

import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models import storage
from os import system

class Hbnb(cmd.Cmd):
    """ the interprator module """
    prompt = '(hbnb) '
    __classes = ['BaseModel', 'User', 'City', 'State', 'Place', 'Amenity', 'Review']

    def do_quit(self, line):
        """ Provides a proper exit to the interpreter """
        return True

    def do_EOF(self, line):
        """ Provides a proper exit with other options """
        return True

    def do_clear(self, line):
        """ Clears the screen """
        system('clear')

    def createInst(self, name, **kwargs) :
        """ Returns an instance based on the class name """

        if (name == 'BaseModel') :
            return BaseModel(**kwargs)

        elif (name == 'User') :
            return User(**kwargs)

        elif (name == 'City') :
            return City(**kwargs)

        elif (name == 'State') :
            return State(**kwargs)

        elif (name == 'Amenity') :
            return Amenity(**kwargs)

        elif (name == 'Review') :
            return Review(**kwargs)

        elif (name == 'Place') :
            return Place(**kwargs)

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id """
        instance = None

        if not line :
            print ("** class name missing **")
            return

        elif line not in Hbnb.__classes :
            print ("** class doesn't exist **")
            return
        else :
            instance = self.createInst(line)
            instance.save()
            print(instance.id)
    
    def __objectExists(self, argv):
        """ Checks if the object exits in the FileStorage.__dict """
        if (len(argv) == 0) :
            print ("** class name missing **")

        elif (argv[0] in Hbnb.__classes) :
            try :
                instId = "{}.{}".format(argv[0], argv[1])
                
                if (instId in storage.all()):
                    return instId
                else :
                    print ("** no instance found **")

            except IndexError :
                print ("** instance id missing **")
        else :
            print ("** class doesn't exist **")
        return False

    def do_show(self, line):
        """ Prints the string representation of an instance based on the class name and id """
        args = line.split()
        key = self.__objectExists(args)
        if key:
            objects = storage.all()
            print (objects[key])

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute 
        (save the change into the JSON file). This method assumes the attribute exists for the instance"""
        args = line.split()
        key = self.__objectExists(args)
        if key :
            objects = storage.all()
            try :
                attr = args[2]
                try :
                    args[3]
                    new_value = self.get_value(' '.join(args[3:]))
                    new_dict = objects[key].to_dict()
                    new_dict[attr] = new_value
                    objects[key] = self.createInst(args[0], **new_dict)

                except IndexError : 
                    print ("** value missing **")
            except IndexError :
                print("** attribute name missing **")

    def get_value(self, args):
        """ return a str without double quotes """
        if (args[0] == args[-1] == '"'):
            return (args[1:-1])
        else :
            return (args)

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id (save the change into the JSON file) """
        args = line.split()
        key = self.__objectExists(args)

        if key :
            objects = storage.all()
            del(objects[key])
            storage.save()

    def do_all(self, line):
        """ Prints all string representation of all instances based or not on the class name """

        objects = storage.all()

        if (line in Hbnb.__classes):
            for key in objects.keys() :
                if (line in key.split(".")):
                    print(objects[key])

        elif not line :
            for key in objects.keys() :
                print(objects[key])
        else :
            print ("** class doesn't exist **")

    def default(self, line):
        """ Overides the defaut method to capture the command """
        args = line.split('.')

        if (len(args) == 2 and args[1][-2:] == '()') :
            cmd = " ".join([args[1].replace('()',''), args[0]])
            self.onecmd(cmd)

        else :
            self.stdout.write('*** Unknown syntax: %s\n'%line)


    def do_sam(self, arg):
        print("Function executed : {}".format(arg))       

    def emptyline(self):
        """Overrides the parent class method"""
