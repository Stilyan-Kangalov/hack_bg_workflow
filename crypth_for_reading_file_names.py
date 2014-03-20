import os
from subprocess import call


def locate_and_run():
    file_name_list = []
    for root, dirs, files in os.walk('./data_base'):
        for file in files:
            file_name_list.append(file)
    return file_name_list
			#print(file)
			#if file.startswith(pattern):
				#call(['python3.3', root + '/' + file])

def main():
    #print(locate_and_run())
    print(locate_and_run())

if __name__ == '__main__':
    main()
