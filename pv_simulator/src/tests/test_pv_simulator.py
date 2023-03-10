import unittest
from datetime import datetime

import numpy as np

from pv_simulator import PVSimulator


class TestPVSimulator(unittest.TestCase):
    data = np.array([
        10,  # 00:00 - 02:00
        20,  # 02:00 - 04:00
        30,  # 04:00 - 06:00
        40,  # 06:00 - 08:00
        50,  # 08:00 - 10:00
        120,  # 10:00 - 12:00
        70,  # 12:00 - 14:00
        110,  # 14:00 - 16:00
        90,  # 16:00 - 18:00
        100,  # 18:00 - 20:00
        80,  # 20:00 - 22:00
        60,  # 22:00 - 24:00
    ])

    def test_draw_value_1(self):
        dt = datetime(2022, 1, 1, 0, 0, 1)
        simulator = PVSimulator(self.data)
        val = simulator.draw_value(dt)
        self.assertEqual(val, self.data[0])

    def test_draw_value_2(self):
        dt = datetime(2022, 1, 1, 1, 59, 59)
        simulator = PVSimulator(self.data)
        val = simulator.draw_value(dt)
        self.assertEqual(val, self.data[0])

    def test_draw_value_3(self):
        dt = datetime(2022, 1, 1, 2, 0, 0)
        simulator = PVSimulator(self.data)
        val = simulator.draw_value(dt)
        self.assertEqual(val, self.data[1])

    def test_draw_value_4(self):
        dt = datetime(2022, 1, 1, 21, 59, 59)
        simulator = PVSimulator(self.data)
        val = simulator.draw_value(dt)
        self.assertEqual(val, self.data[10])

    def test_draw_value_5(self):
        dt = datetime(2022, 1, 1, 23, 59, 59)
        simulator = PVSimulator(self.data)
        val = simulator.draw_value(dt)
        self.assertEqual(val, self.data[11])
