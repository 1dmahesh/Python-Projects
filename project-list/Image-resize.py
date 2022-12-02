from PIL import Image
import os 
cwd = os.getcwd()  

# create a function for image resize
def resize_image(size1, size2):
    image = Image.open(name_pic)
    print("")
    print(f"Current Size : {image.size}")
    
    resized_image = image.resize((size1 , size2))

    resized_image.save(filename)
    print()

name_pic = input("Enter the Image name You want to resize : ")
print()
size1 = int(input('Enter Width Size : '))
print("")
size2  = int(input('Enter Length Size : '))
print("")
filename = 'igamio'+ str(size1) +"_"+ str(size2) + '.png'
resize_image(size1, size2)
print("")
print('Saved File as:' , str(cwd) + '\\'  + str(filename))
print("")

