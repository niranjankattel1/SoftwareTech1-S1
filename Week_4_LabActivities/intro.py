from PIL import Image

image = Image.open('Assets/cat.jpg')
# image.show()

# print(image.size)
# print(image.filename)
# print(image.format)

# hflipped_img = image.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
# vflipped_img = image.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()
# rotated_img = image.transpose(Image.Transpose.ROTATE_90).show()

image.rotate(30).save("Output/rotatedCat.png", "PNG")
