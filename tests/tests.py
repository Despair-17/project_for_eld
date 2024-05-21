import unittest
import os

from database.process_file import *
from core.process_data import *


class TestProcessFile(unittest.TestCase):

    def setUp(self):
        self.test_read_file = 'test_read.csv'
        self.test_write_file = 'test_write.csv'
        self.fieldnames = ['Name', 'Age', 'City']
        self.data = [
            {'Name': 'Alice', 'Age': '30', 'City': 'New York'},
            {'Name': 'Bob', 'Age': '25', 'City': 'Los Angeles'},
            {'Name': 'Charlie', 'Age': '35', 'City': 'Chicago'}
        ]

        with open(self.test_read_file, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=self.fieldnames, delimiter=';')
            writer.writeheader()
            writer.writerows(self.data)

    def tearDown(self):
        if os.path.exists(self.test_read_file):
            os.remove(self.test_read_file)
        if os.path.exists(self.test_write_file):
            os.remove(self.test_write_file)

    def test_read_csv_file(self):
        result = ProcessFile.read_csv_file(self.test_read_file)
        self.assertEqual(result, self.data)

    def test_write_csv_file(self):
        ProcessFile.write_csv_file(self.test_write_file, self.data, self.fieldnames)

        with open(self.test_write_file, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=',')
            result = [row for row in reader]

        self.assertEqual(result, self.data)


class TestProcessDict(unittest.TestCase):

    def test_transform_value_to_range(self):
        data = {'Значение': '10-20'}
        ProcessDict.transform_value_to_range(data)
        expected_range = range(10, 21)
        self.assertEqual(data['Значение'], expected_range)

        data = {'Значение': range(5, 15)}
        ProcessDict.transform_value_to_range(data)
        self.assertEqual(data['Значение'], range(5, 15))

    def test_get_random_dict(self):
        data = [
            {'Значение': range(10, 21)},
            {'Значение': range(5, 15)},
            {'Значение': range(20, 30)},
            {'Значение': range(100, 200)}
        ]

        random_data = ProcessDict.get_random_dict(data, min_count=2, max_count=2)
        self.assertEqual(len(random_data), 2)

        random_data = ProcessDict.get_random_dict(data, min_count=2, max_count=3)
        self.assertTrue(2 <= len(random_data) <= 3)

        for item in random_data:
            self.assertIn(item, data)


class TestProcessRange(unittest.TestCase):

    def test_get_random_value_from_range(self):
        num_range = range(1, 10)

        random_value = ProcessRange.get_random_value_from_range(num_range)
        self.assertIn(random_value, num_range)

        self.assertIsInstance(random_value, int)

        values = {ProcessRange.get_random_value_from_range(num_range) for _ in range(100)}
        self.assertTrue(values.issubset(set(num_range)))
        self.assertGreaterEqual(len(values), 1)


if __name__ == '__main__':
    unittest.main()
