from index
#import global variable

def adding_information_to_txt_file(file_name, name, mail):
    path = 'data_base/'
    filename = file_name + '.txt'
    with open(os.path.join(path, filename), 'a+') as temp_file:
        temp_file.close()
