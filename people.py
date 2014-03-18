class People():
    """docstring for People"""
    def __init__(self, Name, Id = 0):
        self.Name = Name
        self.Id = Id

    def get_name(self):
        return self.Name

    def get_id(self):
        return self.Id

    def push_in_person(self):
        try:
            file = open('person.txt','a+')
            file.write(str(self.Id) + "." + self.Name + "\n")
            file.close()
            return True
        except IOError:
            return False


    def count_rows(self):
        file = open('person.txt', 'r')
        content = file.read()
        print(content)
        if len(content) == 0:
            file.close()
            return 0
        else:
            splited_contents = contents.split('\n')
            count_lines = len(splited_contents)
            file.close()
            return count_lines
