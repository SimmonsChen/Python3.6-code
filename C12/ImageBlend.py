# /usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image

def blend_image():
    im1 = Image.open("one.jpg")
    im1 = im1.convert("RGBA")  # 模式可以为“1”， “L”，“RGBA”
    im2 = Image.open("two.jpg")
    im2 = im2.convert("RGBA")

    im_result = Image.blend(im2, im1, 0.16)  # 注意im2与im1同样的大小
    im_result.save("result1.jpg")
    return_im = im_result.show()
    return return_im


if __name__ == "__main__":
    blend_image()
