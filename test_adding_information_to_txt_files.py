import unittest
from function_for_adding_information_to_txt_file import adding_information_to_txt_file

class adding_test(unittest.TestCase):
    """docstring for adding_test"""
    def test_getting_file_name(self):
        self.assertEqual(True,True)

    def test_adding_information_to_file(self):
        adding_information_to_txt_file('test', 'Rosen', 'rosen@rosen.com')
        file = open('data_base/test.txt', 'r')
        contents = file.read()
        result = contents.split('\n')
        # result.pop()
        # result = result[0]
        file.close()
        self.assertEqual('Rosen rosen@rosen.com', result[0])

    #eventyalno o6te testove

if __name__ == '__main__':
    unittest.main()
