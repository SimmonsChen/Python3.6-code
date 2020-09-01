# /usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw,ImageFont

im = Image.new('RGB', (400, 600), '#000')   #新建黑色图像
font = ImageFont.truetype("simsun.ttc",16)
im1 = Image.open('one.jpg')
resize_im = im1.resize((1200, 800))     # 缩放图像
crop_im = resize_im.crop((500, 200, 900, 500)) # 切割图像
im.paste(crop_im, (0,0)) # 粘贴图像
draw = ImageDraw.Draw(im) # 绘制图像
draw.text((60,350), u'黑夜给了我一双黑色的眼睛',(255,255,255),font=font) # 输入文本
draw.text((60,380),u'我却用它寻找光明',(255,255,255),font=font)
draw.text((60,410),u'——顾城',(255,255,255),font=font)

im2 = Image.open('weixin.jpg')
resize_im2 = im2.resize((120, 120))
im.paste(resize_im2, (180,450))
im.show()