from datetime import datetime

import numpy as np
from PIL import Image


def to_seconds(dt: datetime) -> float:
    midnight = dt.replace(hour=0, minute=0, second=0, microsecond=0)
    return (dt - midnight).total_seconds()


def load_data(pattern_path: str, min_val=0, max_val=3500) -> np.array:
    im = np.asarray(Image.open(pattern_path).convert('L')) # noqa
    mask = np.amax(im, axis=0) == 0

    im = im.shape[0] - np.argmax(im, axis=0)
    im[mask] = 0
    value_range = max_val - min_val
    return im / im.shape[0] * value_range + min_val
