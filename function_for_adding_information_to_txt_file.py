#from index
#import global variable
import os

def adding_information_to_txt_file(file_name, name, mail):
    path = 'data_base/'
    filename = file_name + '.txt'
    with open(os.path.join(path, filename), 'w') as temp_file:
        temp_file.write(str(name) + ' ' + str(mail) + '\n')
        temp_file.close()
