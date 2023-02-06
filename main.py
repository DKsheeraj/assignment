#Imports
from my_package.model import ImageCaptioningModel
from my_package.data.dataset import Dataset
from my_package.data.download import Download
# from my_package.data.transforms import FlipImage, RescaleImage, BlurImage, CropImage, RotateImage
from my_package.data.transforms.flip import FlipImage
from my_package.data.transforms.rotate import RotateImage
from my_package.data.transforms.crop import CropImage
from my_package.data.transforms.blur import BlurImage
from my_package.data.transforms.rescale import RescaleImage
import numpy as np
from PIL import Image


def experiment(annotation_file, captioner, transforms, outputs):
    '''
        Function to perform the desired experiments

        Arguments:
        annotation_file: Path to annotation file
        captioner: The image captioner
        transforms: List of transformation classes
        outputs: Path of the output folder to store the images
    '''

    #Create the instances of the dataset, download
    data = Dataset(annotation_file, transforms)
    down = Download()

    a = data.__len__()

    for i in range (0, a):
        info = data.__getann__(i)
        
        print("file_name: {}".format(info["file_name"]))
        
        list1 = info["captions"]
        for num in list1:
            print(num["caption"])
        print("\n")
        

    for i in range (0, a):
        info = data.__getann__(i)
        url = info["url"]
        path = '/home/datta/Desktop/CS29006_SW_Lab_Spr2023-main/Python_DS_Assignment_Question_02/data/imgs/' + info["file_name"]
        down.__call__(path, url)

    
    img = data.__transformitem__('/home/datta/Desktop/CS29006_SW_Lab_Spr2023-main/Python_DS_Assignment_Question_02/data/imgs/7.jpg')
    img.save('/home/datta/Desktop/mayukha71.jpg')

    #Print image names and their captions from annotation file using dataset object


    #Download images to ./data/imgs/ folder using download object


    #Transform the required image (roll number mod 10) and save it seperately


    #Get the predictions from the captioner for the above saved transformed image  

    print(captioner('/home/datta/Desktop/good.jpeg', 3))


def main():
    captioner = ImageCaptioningModel()
    experiment('./data/annotations.jsonl', captioner, [FlipImage('vertical'), BlurImage(5)], None) # Sample arguments to call experiment()

if __name__ == '__main__' :
    main()
