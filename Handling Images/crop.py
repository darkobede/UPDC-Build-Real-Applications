from PIL import Image

img = Image.open("a.jpg")

area = (100, 100, 200, 200)
cropped_img = img.crop(area)

cropped_img.show()
