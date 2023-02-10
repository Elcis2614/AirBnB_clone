Created by Elisée Busole C.

As the name suggests, this project is about creating an AirBnb web aapplication clone.
The first step to reach that objective will be to write a command interpreter to manage the data from different sources: json files and Mysql database.

1. The command interpreter (consol):

	******** How to start ********

	This module will be built using the cmd module, as a baseclass for our consol.
	The inherited attributes and methods from the cmd module will help to make the consol interactive.

	
	******** How to use it ********

	First, we neeed to create a console class Console, in console.py, that will will inherit the Cmd class, from the cmd module.
	Second, we will provide our class with the do_EOF() method that will enable us to exit the interpreter properly. Other methods will be implemented as the project goes on.
	lastly, outside our console class, we class the Console.cmdloop() method, inherited from the cmd baseclass, which will initiate the looping process when the console.py will be executed.


	******* An example of to use it ********
	1. execute the file, assuming execution permission are granted
	   $ ./console.py
	   $ (hbnb)
	2. Enter any commend included in the Console class. In this case , the quit commend
	   $ (hbnb) quit
	   $ 
	And there we have exited the console
	

