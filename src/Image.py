from PIL import Image, ImageFilter
import os


# in : file name
# out : file path
def getPathImage (imageName):
    
    imageFolder = '../data/'
    
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filePath = imageFolder+imageName
    # print (fileDir)
    # print (filePath)
    filePath = os.path.join(fileDir,filePath);
    # print (filePath)

    filePath = os.path.abspath(os.path.realpath(filePath))
    
    return filePath

# in : file name
# out : image file
def openImage (imageName):

    im = Image.open(getPathImage(imageName))
    return im

# in : file name , image file
# out : //
def saveImage (imageName, image):

    image.save(getPathImage(imageName))
    
# in : file name , image size
# out : image file
def createImage (imageName, size):
    
    newImage = Image.new('RGB',size,100)
    return newImage

def main():
    
    #imageName = "images.jpg"
    #newImage = openImage(imageName)
    
    imageName = "newimage.jpg"
    size = (100,100)
    newImage = createImage (imageName,size)
    saveImage (imageName, newImage)
    
    

    
    
if  __name__ =='__main__':main()