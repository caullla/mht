import unittest
import os
from datetime import datetime
from pathlib import Path

from helper import load_data, to_seconds


BASE_DIR = Path(__file__).resolve().parent
PATTERN_PATH = os.path.join(BASE_DIR, 'sample/sample_mask.png')

class TestHelper(unittest.TestCase):

    def test_load_data(self):
        data = load_data(PATTERN_PATH, 0, 100)
        self.assertEqual(data[2], 0)
        self.assertEqual(data[6], 50)
        self.assertEqual(data[19], 100)

    def test_load_data_with_value_offset(self):
        # test if value range scale according pv pattern
        data = load_data(PATTERN_PATH, 50, 100)
        self.assertEqual(data[2], 50)
        self.assertEqual(data[6], 75)
        self.assertEqual(data[19], 100)

    def test_to_seconds(self):
        dt = datetime(2022, 1, 1, 12, 0, 0)
        seconds = to_seconds(dt)
        self.assertEqual(seconds, 86400 / 2)

    def test_to_seconds(self):
        dt = datetime(2022, 1, 1, 13, 2, 3)
        seconds = to_seconds(dt)
        self.assertEqual(seconds, 86400 / 2 + 60 * 60 + 60 * 2 + 3)

