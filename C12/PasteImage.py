# /usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image


def paste_image():
    base_im = Image.open('two.jpg')  # 加载底图
    base_im = base_im.convert('RGBA')  # 转换成RGBA图像模式

    im1 = Image.open('weixin.jpg')  # #加载需要放上去的图片
    box = (0, 0, 600, 600)

    region = im1.resize((box[2] - box[0], box[3] - box[1])) #对图片进行缩放，以适应box区域大小
    base_im.paste(region, box) #粘贴图片到另一种图片上
    base_im.save('out.jpg')  # 保存图片
    im_show = base_im.show() # 查看合成的图片
    return im_show


if  __name__ == "__main__":
    paste_image()

