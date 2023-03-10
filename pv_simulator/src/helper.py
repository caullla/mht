from datetime import datetime

import numpy as np
from PIL import Image


def to_seconds(dt: datetime) -> float:
    midnight = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return (dt - midnight).total_seconds()


def load_data(pattern_path: str, min_val=0, max_val=3500) -> np.array:
    """
    convert png file into d1 array of power values during the day
    """
    data = np.asarray(Image.open(pattern_path).convert('L')) # noqa

    # mark all columns with values equal 0
    mask = np.amax(data, axis=0) == 0

    data = data.shape[0] - np.argmax(data, axis=0)
    # force replace marked columns with zero
    data[mask] = 0
    value_range = max_val - min_val

    data = data / data.shape[0]
    data = data * value_range + min_val
    return data
