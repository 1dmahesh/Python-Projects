# In this program you can resize any image.
from PIL import Image
import os 
cwd = os.getcwd()  

# This function will be used for resizing image.
def resize_image(size1, size2):
    image = Image.open(name_pic)
    print("")
    print(f"Current Size : {image.size}")
    
    resized_image = image.resize((size1 , size2))

    resized_image.save(filename)
    print()

# Here we will give the image name i.e. = myimage.png

name_pic = input("Enter the Image name You want to resize : ")
print()

# Here we will provide the width size of image.
size1 = int(input('Enter Width Size : '))
print("")

# Here we will provide the Length size of image.
size2  = int(input('Enter Length Size : '))
print("")

#Please provide the new image name here.
filename = 'new-image'+ str(size1) +"_"+ str(size2) + '.png'
resize_image(size1, size2)
print("")
# Here we will print the resized image name and it's path.
print('Saved File as:' , str(cwd) + '\\'  + str(filename))
print("")

