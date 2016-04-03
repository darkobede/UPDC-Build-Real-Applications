from PIL import Image

img = Image.open("a.jpg")
img1 = Image.open("b.jpg")

area = (100, 100, 400, 320)

img1.paste(img, area)

img.show()
