import numpy as np
import math


def mse(im1: np.ndarray, im2: np.ndarray) -> float:
    return ((im1 - im2) ** 2).sum() / im1.size


def psnr(im1: np.ndarray, im2: np.ndarray) -> float:
    return 10 * math.log10(255 ** 2 / mse(im1, im2))


def cos(im1: np.ndarray, im2: np.ndarray) -> float:
    return (im1 * im2).sum() / ((im1 ** 2).sum() * (im2 ** 2).sum())
