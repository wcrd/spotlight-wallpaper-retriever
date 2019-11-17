import os
from shutil import copyfile
from PIL import Image 

# set origin directory information
packages = os.path.expanduser("~\\AppData\Local\Packages\\")
dirNamePartial = "Microsoft.Windows.ContentDeliveryManager_"
dirEnd = "\LocalState\Assets\\"

# set destination directory and file output information
destination = os.path.expanduser("~\\Pictures\Spotlight\\")
fileExt = ".jpg"
minWidth = 1024
skipExisting = True

def landscapeTest(img):
    try:
        i = Image.open(img)
    except:
        return False

    w, h = i.size
    # check image is landscape and meets minimum width
    return (w > h) and (w >= minWidth)

def saveFile(sourcePath, destinationPath):
    if os.path.isfile(destinationPath):
        return 0
    else:
        copyfile(sourcePath, destinationPath)
        return 1

# set counter
counter = 0
for dir in os.listdir(packages):
    # find spotlight package
    if dir.startswith(dirNamePartial):
        # get images dir
        imgDir = packages + dir + dirEnd
        # loop files
        for img in os.listdir(imgDir):
            # if landscape picture export
            if landscapeTest(imgDir+img):
                srcPath = imgDir+img 
                destPath = destination+img
                if skipExisting:
                    counter+=saveFile(srcPath, destPath+fileExt)
                else:
                    while(not saveFile(srcPath, destPath+fileExt)):
                        # rename file
                        destPath = destPath+"(1)"
                    counter+=1
            
print("{} images copied to {}".format(counter, destination))