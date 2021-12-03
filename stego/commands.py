import numpy as np
from PIL import Image
from stego.metrics import cos, mse, psnr

from stego.preprocess import (
    text_to_msg,
    read_file_to_msg,
    bits_to_msg,
    text_from_msg,
    write_fille_from_msg,
    bits_from_msg
)

from stego.transform import inject, eject


def inject_command(
    image_path: str,
    cnt_path: str,
    text: str = None,
    file_path: str = None,
    bits: str = None):
    
    assert image_path.endswith(".png"), "Image is not png"

    msg = np.array([])
    
    if text is not None:
        msg = text_to_msg(text)
    elif file_path is not None:
        msg = read_file_to_msg(file_path)
    elif bits is not None:
        msg = bits_to_msg(bits)
    
    image = np.array(Image.open(image_path))
    cnt = inject(image, msg)

    print("MSE:", mse(image, cnt))
    print("PSNR:", psnr(image, cnt))
    print("COS:", cos(image, cnt))

    Image.fromarray(cnt).save(cnt_path)


def eject_command(
    cnt_path: str,
    message_length: int,
    message_type: str,
    file_path: str = None):

    assert cnt_path.endswith(".png"), "Image is not png"

    cnt = np.array(Image.open(cnt_path))

    msg = eject(cnt, message_length)

    if message_type == "text":
        print(text_from_msg(msg))
    elif message_type == "bits":
        print(bits_from_msg(msg))
    elif message_type == "file":
        assert file_path is not None, "File path is not specified"
        write_fille_from_msg(msg, file_path)
