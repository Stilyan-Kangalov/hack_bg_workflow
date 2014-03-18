import unittest
import people
import os

class people_test(unittest.TestCase):
    """docstring for people_test"""
    def setUp(self):
        self.new_person = people.People("Pesho", 0)
        # self.file = open('person.txt','a+')

    def test_input_name(self):
        self.assertEqual("Pesho", self.new_person.get_name())

    def test_file_open(self):
        self.assertEqual(True, self.new_person.push_in_person())

    def test_id(self):
        result = self.new_person.count_rows()
        self.new_person.push_in_person()
        self.assertEqual(result, self.new_person.get_id())

    def test_person_txt_file(self):
        result = self.new_person.push_in_person()
        self.assertEqual(True, result)
        file = open('people.txt','r')
        content = file.read()
        file.close()
        self.assertEqual("1.Pesho",content)

    def tearDown(self):
        # self.file.close()
        os.remove('person.txt')

if __name__ == '__main__':
    unittest.main()
