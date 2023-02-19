from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

for i in range(0,2):

    imie=input()

    listagosci = open("lista_gosci/lista_gosci_"+imie+".txt", "r")
    
    img = Image.open("wzory/wzor_"+imie+".jpg")
    
    I1 = ImageDraw.Draw(img)
    
    font=ImageFont.truetype('StylishCalligraphyDemo-XPZZ.ttf', 200)
    
    while(True):
        gosc = listagosci.readline()
        
        if not gosc:
            break
        
        I1.text((600,2175), gosc, font=font, fill=(255,255,255))
        
        img.save("gotowe_zaproszenia_"+imie+"/"+str(gosc)+".jpg")
    
    listagosci.close()
    
    img.close()