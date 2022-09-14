
from PIL import Image, ImageFilter,ImageEnhance

im = Image.open("download.jpg")
im2 = Image.open("imageh.jpg")
im3 = Image.open("poo.webp")
# im2.filter(ImageFilter.EMBOSS).show()
# im2.filter(ImageFilter.CONTOUR).show()
# im2.filter(ImageFilter.FIND_EDGES).show()
# im2.filter(ImageFilter.BLUR).show()
# im3.filter(ImageFilter.SHARPEN).show()
# im2.filter(ImageFilter.SMOOTH).show()
# im2.filter(ImageFilter.MaxFilter(3)).show()
# im2.filter(ImageFilter.MinFilter(3)).show()
# im2.filter(ImageFilter.MedianFilter(5)).show()

# aim = ImageEnhance.Color(im2)
# for i in range(-10,11,2):
#     aim.enhance(i).show()

imc = im3.copy()
img = im.copy()
im3_s = im3.resize((300,240))
imc.paste(im3_s, (700,0))
imc.paste(im3_s, (0,0))
imc.paste(img, (950,642))
imc.show()

