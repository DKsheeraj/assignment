#Imports
from PIL import Image
import random

class CropImage(object):
    '''
        Performs either random cropping or center cropping.
    '''

    def __init__(self, shape, crop_type='center'):
        '''
            Arguments:
            shape: output shape of the crop (h, w)
            crop_type: center crop or random crop. Default: center
        '''
        self.shape = shape
        self.crop_type = crop_type

    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)
            Returns:
            image (numpy array or PIL image)
        '''
        im = Image.open(image)

        if(self.crop_type == 'center'):
            xcen = im.width/2
            ycen = im.height/2
            w = self.shape[1]
            h = self.shape[0]

            xleft = xcen - (w/2)
            xright = xcen + (w/2)
            ytop = ycen - (h/2)
            ybottom = ycen + (h/2)

            imim = im.crop((xleft, ytop, xright, ybottom))

        else:
            xcen = random.randint(1,im.width)
            ycen = random.randint(1, im.height)

            w = self.shape[1]
            h = self.shape[0]

            xleft = xcen - (w/2)
            xright = xcen + (w/2)
            ytop = ycen - (h/2)
            ybottom = ycen + (h/2)

            imim = im.crop((xleft, ytop, xright, ybottom))

        
        return imim

# tu = (50, 50)
# image = CropImage(tu, 'random')
# im = image.__call__("/home/datta/Desktop/index.jpeg")
# im.show()

 