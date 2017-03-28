from PIL import Image, ImageDraw, ImageFont

def add_num(img):
	draw = ImageDraw.Draw(img)
	myfont = ImageFont.truetype('arial.ttf', size = 40)
	fillcolor = '#ff0000'
	width, height = img.size
	draw.text((width - 40 * 2, 0), '99', font = myfont, fill = fillcolor)
	img.save('result.jpg', 'jpeg')
	return 0

if __name__ == '__main__':
	image = Image.open('huaji.jpg')
	add_num(image)
