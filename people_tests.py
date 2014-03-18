import unittest
import people

class people_test(unittest.TestCase):
    """docstring for people_test"""
    def setUp(self):
        self.new_person = people.People("Pesho", 0)

    def test_input_name(self):
        self.assertEqual("Pesho", self.new_person.get_name())

    def test_file_open(self):
        self.assertEqual(True, self.new_person.push_in_person())

    def test_id(self):
        reuslt = new_person.count_rows()
        self.assertEqual(result + 1, self.new_person.get_id())

    def test_person_txt_file(self):
        file = open(people.txt,'a+')
        content = file.read()
        self.assertEqual("1.Pesho",content)

