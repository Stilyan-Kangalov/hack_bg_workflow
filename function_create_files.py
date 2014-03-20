import os

def create_files(file_name):
    path = 'data_base/'
    if not os.path.exists(path):
        os.makedirs(path)

    filename = file_name + '.txt'
    # file = open(filename, 'a+')
    # file.close()
    with open(os.path.join(path, filename), 'a+') as temp_file:
        temp_file.close()

if __name__ == '__main__':
    create_files('newtxttt')
