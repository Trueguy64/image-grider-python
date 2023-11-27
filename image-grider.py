import cv2;
import os

#imageInput = input('What is Your File Name (With extension)?: ')
#rowInput = int(input('Numbers of rows: '))
#columnInput = int(input('Numbers of columns: '))
#fileName = input('Name of Output File: ')
#fileExt = input('File Extension Output With Dot(e.g. .PNG, .JPG): ')
#path = input('Where do you want to save it?: ')

image = cv2.imread(str(imageInput), cv2.IMREAD_UNCHANGED)
dimensions = image.shape
height = dimensions[0]/columnInput
width = dimensions[1]/rowInput
ranger = (rowInput*columnInput)
h = 0
w = 0
dw = width
dh = height
for i in range(ranger):
    if i == 0:
        croppedImage = image[int(h):int(height),int(w):int(width)]
        cv2.imwrite(os.path.join(str(path),str(fileName)+str(i)+str(fileExt)),croppedImage)
    else:
        if width == dimensions[1]:
            h+=dh
            height+=dh
            width = dimensions[1]/rowInput
            w = 0
            croppedImage = image[int(h):int(height),int(w):int(width)]
            cv2.imwrite(os.path.join(path,str(fileName)+str(i)+str(fileExt)),croppedImage)
        else:
            w+=dw
            width+=dw
            croppedImage = image[int(h):int(height),int(w):int(width)]
            cv2.imwrite(os.path.join(path,str(fileName)+str(i)+str(fileExt)),croppedImage)
            print(str(i)+", "+str(w)+":"+str(width)+", "+str(h)+":"+str(height))
