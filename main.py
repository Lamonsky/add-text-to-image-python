from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

listagosci = open("lista_gosci.txt", "r")

img = Image.open("wzor.jpg")

I1 = ImageDraw.Draw(img)

font=ImageFont.truetype('StylishCalligraphyDemo-XPZZ.ttf', 200)

while(True):
    gosc = listagosci.readline()
    if not gosc:
        break
    I1.text((600,2175), gosc, font=font, fill=(255,255,255))
    img.save(str(gosc)+".jpg")