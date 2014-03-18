# Main part - run tests

import unittest
import mails

class people_test(unittest.TestCase):
    """docstring for mail_test"""
    def setUp(self):
        self.new_mail = mail.basemail("pesho@abv.bg", 0)

    def test_input_name(self):
        self.assertEqual("pesho@abv.bg", self.new_mail.get_mail())

    def test_file_open(self):
        self.assertEqual(True, self.new_mail.push_in_mail())

    def test_id(self):
        reuslt = new_person.count_rows()
        self.assertEqual(result + 1, self.new_mail.get_id())

    def test_person_txt_file(self):
        file = open(mails_dir.txt,'a+')
        content = file.read()
        self.assertEqual("1.pesho@abv.bg",content)

if __name__ == '__main__':
	unittest.main()