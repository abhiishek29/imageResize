from PIL import Image 
from argparse import ArgumentParser
from sys import exit
from os import listdir, path, mkdir
from time import time

#####################################
# Specify Path for Default Folder
pathName = "D:/ResiZed/"
# End with '/'
#####################################

# To get the extension of Image
def getImageData(image):
    # image = image.filename.split("/")[-1]
    image = path.basename(image.filename)
    return (image.split(".")[0], image.split(".")[1])

# Actual resize Function
def resizeImage(height,width,image):
    name, extension = getImageData(image)
    img = image.resize((height, width), Image.ANTIALIAS)
    try:
        print(pathName+name+"."+extension)
        img.save(pathName+name+"."+extension)
        print("[SUCCESS] Image Saved - "+pathName+name+"."+extension+str(img.size))
    except:
        print("Couldn't Save Image.")

# To get the dimensions for the new image
def dimensions(height_argument, width_argument, size):
    # To Maintain Aspect Ratio
    if args["maintainAspect"]:
        print("[INFO] Maintaining Aspect Ratio")
        if height_argument-400:
            width_argument = int((height_argument/size[0])*size[1])
        else:
            height_argument = int((width_argument/size[1])*size[0])
    return (height_argument, width_argument)

# Main Function
def processImage(filename):
    # Initialize Variables
    new_h = args["height"]
    new_w = args["width"]
    try:
        filename = filename.replace("\\", "/")
        print("[INFO] Processing Image: "+filename)
        img = Image.open(filename)
    except:
        print("Could not open file. Check path or file name.")
        exit()
    new_h, new_w = dimensions(new_h, new_w, img.size)
    resizeImage(new_h, new_w, img)

ap = ArgumentParser()
ap.add_argument("-i", "--image", default=None, help="path to input image")
ap.add_argument("-d", "--directory", default=None, help="path to input directory")
ap.add_argument("-l", "--height", default=400, type=int, help="height for new image(default=400)")
ap.add_argument("-b", "--width", default=400, type=int, help="width for new image(default=400)")
ap.add_argument("-a", "--maintainAspect", default=False, type=bool, help="True: Don't change the aspect ratio.")
args = vars(ap.parse_args())

# Checking for output folder Directory
if path.isdir(pathName) == False:
    mkdir(pathName)

if args["image"]:
    processImage(args["image"])
elif args["directory"]:
    if args["directory"][-1] not in ["/","\\"]:
        args["directory"]+="/"
    for f in listdir(args["directory"]):
        processImage(args["directory"]+f)
else:
    print("You know you have to pass arguments!!")
