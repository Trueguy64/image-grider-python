#Imports necessary modules, which is OpenCV for modifying the image, and OS for where to save the grided images
import cv2;
import os

#Inputs for gridding the image
imageInput = input('What is Your File Name (With extension)?: ')
rowInput = int(input('Numbers of rows: '))
columnInput = int(input('Numbers of columns: '))
fileName = input('Name of Output File: ')
fileExt = input('File Extension Output With Dot(e.g. .PNG, .JPG): ')
path = input('Where do you want to save it?: ')

"""
Reads the inputs provided by the user 
'cv2.IMREAD_UNCHANGED' is added so that the final images retains it's original data aside from it's dimensions
"""
image = cv2.imread(str(imageInput), cv2.IMREAD_UNCHANGED)
#Gets the dimensions of the image
dimensions = image.shape

#Gets the height of the image by the dimensions as the zero'th in the array and divides by the columns requested by the user to get the length of each column
height = dimensions[0]/columnInput
#Gets the width of the image by the dimensions as the first in the array and divides by the rows requested by the user to get the length of each row
width = dimensions[1]/rowInput
#The ranger multiplies the amount of rows and columns to get the amount of repetition required to output all the gridded images
ranger = (rowInput*columnInput)

#h and w are variables for the starting points of where the width or height begins
h = 0
w = 0
#dw is the width constant of the image
dw = width
#dh is the height constant the image
dh = height


#This for loop divides the image itself, where ranger is the variable 
for i in range(ranger):
    #Checks if the the width variable reaches the maximum length, where it will go down to the next row, and resets both width and w
    if width == dimensions[1]:
            h+=dh
            height+=dh
            width = dimensions[1]/rowInput
            w = 0
    #Checks the i variable if it is not zero, where the program will go to the next column of the image
    elif i != 0:
        w+=dw
        width+=dw
        croppedImage = image[int(h):int(height),int(w):int(width)]
        cv2.imwrite(os.path.join(path,str(fileName)+str(i)+str(fileExt)),croppedImage)
        print(str(i)+", "+str(w)+":"+str(width)+", "+str(h)+":"+str(height))
croppedImage = image[int(h):int(height),int(w):int(width)]
cv2.imwrite(os.path.join(path,str(fileName)+str(i)+str(fileExt)),croppedImage)
