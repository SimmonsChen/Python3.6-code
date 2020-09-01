# /usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image


def composite_image():
    im1 = Image.open("one.jpg")
    im1 = im1.convert("RGBA") # 模式可以为“1”， “L”，“RGBA”
    im2 = Image.open("two.jpg")
    im2 = im2.convert("RGBA")
    r, g, b, alpha = im2.split()
    alpha = alpha.point(lambda i: i > 0 and 161)

    im_result = Image.composite(im2, im1, alpha) # 注意im2与im1同样的大小
    im_result.save("result1.jpg")
    return_im = im_result.show()
    return return_im


if  __name__ == "__main__":
    composite_image()
