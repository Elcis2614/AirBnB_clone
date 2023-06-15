#!/usr/bin/python3
""" Implementation of the interpretor """

import cmd
from models.base_model import BaseModel
from models import storage

class Hbnb(cmd.Cmd):
    """ the interprator module """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """ Provides a proper exit to the interpreter """
        return True

    def do_EOF(self, line):
        """ Provides a proper exit with other options """
        return True

    def do_create(self, line):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id """
        if not line :
            print ("** class name missing **")

        elif (line == 'BaseModel') :
            instance = BaseModel()
            instance.save()
            print(instance.id)

        else :
            print ("** class doesn't exist **")
    
    def __objectExists(self, argv):
        """ Checks if the object exits in the FileStorage.__dict """
        if (len(argv) == 0) :
            print ("** class name missing **")

        elif (argv[0] == "BaseModel") :
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
                    new_value = args[3]
                    new_dict = objects[key].to_dict()
                    if (attr in new_dict):
                        if (type(new_value) != type(new_dict[attr])):
                            print ("Not same type")
                            print ("Type on new_value : {} , type of old : {} ".format(new_value, objects[key]))
                            return

                    new_dict[attr] = new_value
                    objects[key] = BaseModel(**new_dict)
                    objects[key].save()

                except IndexError : 
                    print ("** value missing **")
            except IndexError :
                print("** attribute name missing **")
        
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
        validClasses = ['BaseModel']
        objects = storage.all()

        if (line in validClasses):
            for key in objects.keys() :
                if (line in key.split(".")):
                    print(objects[key])

        elif not line :
            for key in objects.keys() :
                print(objects[key])
        else :
            print ("** class doesn't exist **")

    def emptyline(self):
        """Overrides the parent class method"""
