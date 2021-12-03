import numpy as np


def read_file_to_msg(path: str) -> np.ndarray:
    with open(path, "rb") as fp:
        return np.frombuffer(fp.read(), dtype=np.uint8)


def text_to_msg(text: str) -> np.ndarray:
    return np.frombuffer(text.encode(), dtype=np.uint8)


def bits_to_msg(bits: str) -> np.ndarray:
    return np.array([int(bits[i:i + 8], 2) for i in range(0, len(bits), 8)], dtype=np.uint8)
