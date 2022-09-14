from PIL import Image

im = Image.open("download.jpg")
im2 = Image.open("imageh.jpg")

print("rsolution",im.size)
print("height",im.height)
print("width",im.width)
print("mode",im.mode)
print("format",im.format)
print("exif",im.info)

im.convert("L").show()

im.resize((100,100)).show() #down scaling # choti karna
im.resize((2000,2000)).show()  #up scaling

im.resize((im.width*5,im.height*5)).save("duck.jpg")