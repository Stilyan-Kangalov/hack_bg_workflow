# Import section

#from people import *
#from mails import *

# Define main section with functions

# -- Parse the command input from the terminal

def get_command(command):
    return tuple(command.split(" "))


def is_command(fixed_command, command_string):
    return fixed_command[0] == command_string

# Set-up some empty vars + "password vars" for identification:
control = []
register_box = {}
code_register = 3015
code_save = 1045



# Set-up the base functions 

def run_unknown_command():
	command_error = ["Error: Unknown command!",
                       "Try one of the following:",
                       " register <name> <e-mail>",
                       " unique <e-mail>",
                       " search",
                       " merge",
                       " export",
                       " finish"]
	for line in command_error:
		print(line)


def run_help(fixed_command):
	command_help = ["Great, you choose \'help\' command!",
                       "Try one of the following:",
                       " register <name> <e-mail>",
                       " unique <e-mail>",
                       " search",
                       " merge",
                       " export",
                       " finish"]
	for line in list(command_help):
		print(line)	

def sample():
	print(register_box)

def run_register(fixed_command):
	if len(fixed_command) != 3:
		print("You can't use it in that way, please try again!")
	else:
		print("Taking registration from %s with %s as e-mail adress." % (fixed_command[1], fixed_command[2]))
		register_box[fixed_command[1]] = fixed_command[2]
		control.append(code_register)

		if len(register_box) != 0:
			while True:
				n = input("Please confirm by entering 'yes' or 'no':")
				if n.strip() == 'no':
					print("Your entry was rejected.")
					register_box.clear()
					break
				if n.strip() == 'yes':
					print("Your entry was saved")
					sample()
					break


def run_finish(fixed_command):
	if code_save not in control:		
		msg = ["You haven't made any registration.",
		            "If you wish to exit, type <finish> again.",
		            "If you want to make registration in the system, type <register> <name> <e-mail>."]

		for line in msg:
			print(line)

		control.append(code_save)
	elif code_save in control:
		exit("Everything clear. Goodbye!")

# Set-up the main function:

def main():
   	while True:
   		print ("If you need tip, enter <help> command:")
   		command = get_command(input("Enter command>")) 

   		if is_command(command, "register"):
   			run_register(command)

   		elif is_command(command, "unique"):
   			run_unique(command)
   		
   		elif is_command(command, "search"):
   			run_search(command)

   		elif is_command(command, "merge"):
   			run_merge(command)

   		elif is_command(command, "help"):
   			run_help(command)	

   		elif is_command(command, "export"):
   			run_export(command)

   		elif is_command(command, "finish"):
   			run_finish(command)   		

   		else:
   			run_unknown_command() 

# Run the main function

if __name__ == '__main__':
    main()            