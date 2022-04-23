from PIL import Image
import os
from pathlib import Path

file_path = Path(r"YourimageFilepath/")

def compress_images(directory=False, quality=30):
    #if directory path exist, change to that directory
    if directory:
        os.chdir(directory)
    
    #fetch all files in directory
    files = os.listdir()

    #only for specific image file extension
    images = [file for file in files if file.endswith(('.jpg','.png'))]

    #Loop over every image
    for image in images:
        
        img = Image.open(image)

        img.save('Compress_img_' + image, optimize = True, quality=quality)

compress_images(file_path)