from crypth_for_reading_file_names import locate_and_run

def show_list():
    i = 1
    for item in locate_and_run():
        print(i,'.',item)
        i+=1

if __name__ == '__main__':
    show_list()
