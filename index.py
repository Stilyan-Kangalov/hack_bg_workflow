# Import section

import people
import mails

# Define main section with functions

# -- Parse the command input from the terminal

def get_command(command):
    return tuple(command.split(" "))


def is_command(fixed_command, command_string):
    return fixed_command[0] == command_string

# Set-up some empty vars:

code_save = 1045



# Run 

def run_unknown_command():
	command_error = ["Error: Unknown command!",
                       "Try one of the following:",
                       " register <name> <e-mail>",
                       " unique",
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
                       " unique",
                       " search",
                       " merge",
                       " export",
                       " finish"]
	for line in list(command_help):
		print(line)	


def run_finish(fixed_command):
	if code_save not in control:		
		msg = ["You haven't made any registration.",
		            "If you wish to exit, type finish again.",
		            "If you want to make registration in the ststem, type <register> <name> <e-mail>."]

		for line in msg:
			print(line)

		control.append(code_save)
	elif code_save in control:
		exit("Everything clear. Goodbye!")

# Start the main funvtion:

def main():
   	while True:
   		print ("If you need tip, enter <help> command:")
   		command = get_command(input("Enter command>")) 

   		if is_command(command, "register"):
   			run_take(command)

   		elif is_command(command, "unique"):
   			run_status(command)
   		
   		elif is_command(command, "search"):
   			run_save(command)

   		elif is_command(command, "merge"):
   			run_list(command)

   		elif is_command(command, "help"):
   			run_help(command)	

   		elif is_command(command, "export"):
   			run_load(command)

   		elif is_command(command, "finish"):
   			run_finish(command)   		

   		else:
   			run_unknown_command() 

# Run the main function

if __name__ == '__main__':
    main()            