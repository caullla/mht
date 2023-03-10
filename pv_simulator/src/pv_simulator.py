import math
from datetime import datetime

import numpy as np

from helper import to_seconds

TOTAL_DAY_SECONDS = 60 * 60 * 24


class PVSimulator:
    def __init__(self, data: np.array, deviation: float = 0.03) -> None:
        self.data = data
        self.deviation = deviation

    def draw_value_with_deviation(self, current_dt: datetime) -> float:
        value = self.draw_value(current_dt)
        value = value * (1 + np.random.uniform(self.deviation * -1, self.deviation))
        return round(value, 2)

    def draw_value(self, current_dt: datetime) -> float:
        seconds = to_seconds(current_dt)
        offset = seconds / TOTAL_DAY_SECONDS
        index = math.floor(offset * self.data.shape[0])
        return round(self.data[index], 2)

