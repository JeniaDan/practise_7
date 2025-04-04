import unittest
from app.io.input import read_file

class TestReadFile(unittest.TestCase):

    def test_read_file_exists(self):
        """
        Test if the function correctly reads an existing text file.
        """
        file_path = input("Enter the path to a text file (e.g., data/test_file.txt): ")
        self.assertEqual(read_file(file_path), "Hello, World!")

    def test_read_file_not_found(self):
        """
        Test if the function correctly handles the case when the file is not found.
        """
        file_path = input("Enter the path to a non-existent file: ")
        self.assertTrue("Error" in read_file(file_path))

    def test_read_file_empty(self):
        """
        Test if the function correctly handles an empty file.
        """
        file_path = input("Enter the path to an empty file (e.g., data/empty_file.txt): ")
        self.assertEqual(read_file(file_path), "")

if __name__ == "__main__":
    unittest.main()