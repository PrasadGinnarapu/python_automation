"""importing the module"""
import sys

from PIL import Image
import os

def heicimagecon():
    im = Image.open(image_name)
    print("The size of the image before conversion : ", end="")
    print(os.path.getsize(image_name))

            # converting to jpg
    rgb_im = im.convert("RGB")

            # exporting the image
    rgb_im.save("heic_to_jpg.jpg")
    print("The size of the image after conversion : ", end="")
    print(os.path.getsize("heic_to_jpg.jpg"))




def pngimageconv():


    im = Image.open(image_name)
    print("The size of the image before conversion : ", end="")
    print(os.path.getsize(image_name))

    # converting to jpg
    rgb_im = im.convert("RGB")

    # exporting the image
    rgb_im.save("png_to_jpg.jpg")
    print("The size of the image after conversion : ", end="")
    print(os.path.getsize("png_to_jpg.jpg"))


while True:
    yesno = input("Do you want to convert Imges?(Y/N): ").upper()
    if yesno == 'Y':
        image_name = input('Enter imagename with extension: ')
        ext = image_name.split('.')
        ext = ext[1:]
        if ext[0] == 'jpg':
            print("Sorry, The file already in JPG format")
        elif ext[0] == '00de8048-78f8-4c72-8a95-76bd7e516518':
            heicimagecon()
        elif ext[0] == 'png':
            pngimageconv()
        else:
            sys.exit()


    else:
        sys.exit()





