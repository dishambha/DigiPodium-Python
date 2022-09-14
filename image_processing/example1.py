from PIL import Image

im = Image.open("download.jpg")
im2 = Image.open("imageh.jpg")

print(im)
print(im2)

im.rotate(45).show()
im2.rotate(90).show()