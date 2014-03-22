# Import section

#from people import *
#from mails import *
from sys import exit
import os
from subprocess import call

# Define main section with functions

# -- Parse the command input from the terminal

def get_command(command):
    return tuple(command.split(" "))


def is_command(fixed_command, command_string):
    return fixed_command[0] == command_string

# Set-up some empty vars + "password vars" for identification:
control = []
register_box = {}
files_list = []
code_register = 3015
code_save = 1045



# Set-up the base functions 

def run_unknown_command():
	command_error = ["Here is a full list of commands:",
                       "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
                       "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
                       "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
                       "* create <list_name> - Creates a new empty list, with the given name.",
                       "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
                       "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
                       "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
                       "* exit - this will quit the program"]
	for line in command_error:
		print(line)


def run_help(fixed_command):
	command_help = ["Here is a full list of commands:",
                       "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
                       "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
                       "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
                       "* create <list_name> - Creates a new empty list, with the given name.",
                       "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
                       "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
                       "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
                       "* exit - this will quit the program"]
	for line in list(command_help):
		print(line)	
'''
def update_filelist():	

	with open("all_lists.txt", "a") as f:
			for l in files_list:
				bo = files_list.index(l)
				f.write(str(bo))
				f.write(" - ")
				f.write(l)
				f.write("\n")
	f.close()				

def run_create(fixed_command):	
	filename = fixed_command[1]
	files_list.append(filename)
	target = open (filename, 'w+')
	#print(files_list)
	update_filelist()
	target.close()
	files_list.clear()
	print("Your list has been created.")
'''
# Define Class:

class MailList(object):
	"""basic file functions for MailList"""
	def __init__(self, arg):
		self.arg = arg

	def create_files(self):
		path = 'data_base/'
		if not os.path.exists(path):
			os.makedirs(path)

		filename = self[1] + '.txt'
		# file = open(filename, 'a+')
		# file.close()
		with open(os.path.join(path, filename), 'a+') as temp_file:
			temp_file.close()

	'''def locate_and_run(self):
		file_name_list = []
		for root, dirs, files in os.walk('./data_base'):
			for file in files:
				file_name_list.append(file)
		return file_name_list'''

	def show_lists(self):
		file_name_list = []
		for root, dirs, files in os.walk('./data_base'):
			for file in files:
				file_name_list.append(file)
		#return file_name_list

		i = 1
		for item in file_name_list:
			print(i,'-',item)
			i+=1

	def show_list(self):
		path = 'data_base/'
		filename = self[1]
		with open(os.path.join(path, filename), 'r') as temp_file:
			contents = temp_file.read()
			print(contents)
			temp_file.close()

# for refactioring
	def adding_information_to_txt_file(file_name, name, mail):
		path = 'data_base/'
		filename = file_name + '.txt'
		with open(os.path.join(path, filename), 'a+') as temp_file:
			temp_file.close()					

new_list = MailList		

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

   		if is_command(command, "create"):
   			new_list.create_files(command)

   		elif is_command(command, "add"):
   			new_list.adding_information_to_txt_file(command)

   		elif is_command(command, "show_lists"):
   			new_list.show_lists(command)

   		elif is_command(command, "show_list"):
   			new_list.show_list(command)			
  		
   		elif is_command(command, "search_email"):
   			run_search_in_mails(command)

   		elif is_command(command, "merge_lists"):
   			run_merge(command)

   		elif is_command(command, "help"):
   			run_help(command)	

   		elif is_command(command, "export"):
   			run_export(command)

   		elif is_command(command, "exit"):
   			run_finish(command)   		

   		else:
   			run_unknown_command() 

# Run the main function

if __name__ == '__main__':
    main()            