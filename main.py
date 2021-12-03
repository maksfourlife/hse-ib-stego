import numpy as np
from PIL import Image
from stego import eject, inject


im = np.array(Image.open("../image.png"))
ctr = inject(im, np.array([1, 2, 3, 4, 5]))
msg = eject(ctr, 5)

print(msg)
