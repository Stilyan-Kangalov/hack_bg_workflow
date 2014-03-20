def show_list(file_name):
    path = 'data_base/'
    filename = file_name
    with open(os.path.join(path, filename), 'r') as temp_file:
        contents = temp_file.read()
        print(contents)
        temp_file.close()
