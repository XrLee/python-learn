# coding:utf-8
"""this script add some text to a picture"""

from PIL import Image, ImageDraw, ImageFont

def add_num(img):
    """add text to a picture

    Args:
    img: a picture

    """
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('C:/windows/fonts/simhei.ttf', size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 40 * 6, 0), unicode('还好有时光机', 'utf-8'), font=myfont, fill=fillcolor)
    img.save('result.jpg', 'jpeg')
    img.show()
    return 0

if __name__ == '__main__':
    IMAGE = Image.open('huaji.jpg')
    add_num(IMAGE)
