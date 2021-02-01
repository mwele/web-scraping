from PIL import Image
import subprocess
def cleanFile(filePath, newFilePath):
    image = Image.open(filePath)
    #Set a threshold value for the image, and save
    image = image.point(lambda x: 3 if x<143 else 255)
    image.save(newFilePath)
    #call tesseract to do OCR on the newly created image
    subprocess.call(["tesseract", newFilePath, "output"],shell=True)
    #Open and read the resulting data file
    outputFile = open("output.txt", 'r')
    print(outputFile.read())
    outputFile.close()
cleanFile("image.jpg", "image_clean.jpg")
'''This error is because i run above command in a window shell, but do not specify the shell=True argument in subprocess module’s run method. 
After i add shell=True argument in subprocess module’s run method, it runs successfully like below.'''