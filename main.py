from PIL import Image, ImageEnhance, ImageFilter

import os

path = './imgs'
pathOut  = '/editedImgs'

for filename in os.listdir(path): #loop through all files in the folder
    img = Image.open(path + '/' + filename) #open the file 

    edit = img.filter(ImageFilter.SHARPEN).rotate(-90) #edit the file

    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit) 
    edit = enhancer.enhance(factor) 

    clean_name = os.path.splitext(filename)[0] #get the name of the file

    edit.save(pathOut + '/' + filename) #save the file