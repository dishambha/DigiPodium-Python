from PIL import Image, ImageDraw,ImageFont,ImageFilter

im = Image.open("download.jpg")
im2 = Image.open("imageh.jpg")
im3 = Image.open("poo.webp")
im3.filter(ImageFilter.SHARPEN)
font = ImageFont.truetype(r"C:\Windows\Fonts\BAUHS93.TTF",140)
font2 = ImageFont.truetype(r"C:\Windows\Fonts\BAUHS93.TTF",40)

imd = ImageDraw.Draw(im3)

imd.text((2,1),"cartoon",fill=(255,1,100),font=font, )
imd.text((800,700),"cartoon",fill=(0,0,0),font=font2, )
im3.save("edited_poo.webp")
