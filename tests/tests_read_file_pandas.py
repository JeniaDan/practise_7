import unittest
import pandas as pd
from app.io.input import read_file_pandas

class TestReadFilePandas(unittest.TestCase):

    def test_read_file_pandas_exists(self):
        """
        Test if the function correctly reads an existing CSV file.
        """
        file_path = input("Enter the path to a CSV file (e.g., data/test_file.csv): ")
        df = read_file_pandas(file_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (3, 2))

    def test_read_file_pandas_not_found(self):
        """
        Test if the function correctly handles the case when the CSV file is not found.
        """
        file_path = input("Enter the path to a non-existent CSV file: ")
        self.assertTrue("Error" in read_file_pandas(file_path))

    def test_read_file_pandas_invalid_format(self):
        """
        Test if the function correctly handles the case when the file is not a CSV.
        """
        file_path = input("Enter the path to a non-CSV file (e.g., data/invalid_file.txt): ")
        with open(file_path, "w") as f:
            f.write("This is not a CSV file")
        self.assertTrue("Error" in read_file_pandas(file_path))

if __name__ == "__main__":
    unittest.main()