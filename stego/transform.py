import numpy as np
from tqdm import trange


def inject(image: np.ndarray, msg: np.ndarray) -> np.ndarray:
    shape = image.shape
    image = image.copy().reshape((-1,))

    image_mask = 1
    for i in trange(msg.size, desc="injection"):
        for j in range(8):
            k = (i * 8 + j) % image.size

            if k == image.size - 1:
                image_mask *= 2
            
            image[k] = image[k] & ~image_mask | msg[i] >> (7 - j) & 1

    image = image.reshape(shape)
    return image


def eject(ctr: np.ndarray, msg_length: int) -> np.ndarray:
    ctr = ctr.reshape((-1,))
    msg = np.zeros((msg_length,), dtype=np.uint8)

    ctr_mask = 1
    for i in trange(msg.size, desc="ejection"):
        for j in range(8):
            k = (i * 8 + j) % ctr.size

            if k == ctr.size - 1:
                ctr_mask *= 2

            msg[i] |= (ctr[k] & ctr_mask) << (7 - j)

    return msg
