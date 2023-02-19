from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

listagosci = open("lista_gosci.txt", "r")

img = Image.open("wzor.jpg")

I1 = ImageDraw.Draw(img)

font=ImageFont.truetype('NotoSansMono-Black.ttf', 65)

while(True):
    gosc = listagosci.readline()
    if not gosc:
        break
    I1.text((28,36), gosc, font=font, fill=(0,0,0))
    img.save(str(gosc)+".jpg")