import cv2;
import os

image = cv2.imread('OneShot_Niko_Spritesheet.png', cv2.IMREAD_UNCHANGED)
dimensions = image.shape
height = dimensions[0]
width = 97
h = 0
w = 0
x = 24
path = '/home/veronica/Pictures/Niko Stickers/'
for i in range(8):
    if i == 0:
        croppedImage = image[291:388,w:int(width)]
        cv2.imwrite(os.path.join(path,"Niko"+str(x)+".png"),croppedImage)
    else:
        x+=1
        w+=97
        width=97
        width=width*(i+1)
        croppedImage = image[291:388,w:int(width)]
        cv2.imwrite(os.path.join(path,"Niko"+str(x)+".png"),croppedImage)
        print(str(i)+", "+str(w)+":"+str(width)+", "+str(h)+":"+str(height))
