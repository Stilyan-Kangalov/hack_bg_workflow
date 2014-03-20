import os
from subprocess import call
 
 
def locate_and_run():
	for root, dirs, files in os.walk('./tt1'):
		for file in files:
			print(file)
			#if file.startswith(pattern):
				#call(['python3.3', root + '/' + file])
 
 
def main():
	locate_and_run('tests')
 
 
if __name__ == '__main__':
	locate_and_run()