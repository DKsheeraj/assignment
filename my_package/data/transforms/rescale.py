#Imports
from PIL import Image

class RescaleImage(object):
    '''
        Rescales the image to a given size.
    '''

    def __init__(self, output_size):
        '''
            Arguments:
            output_size (tuple or int): Desired output size. If tuple, output is
            matched to output_size. If int, smaller of image edges is matched
            to output_size keeping aspect ratio the same.
        '''
        self.output_size = output_size


    def __call__(self, image):
        '''
            Arguments:
            image (numpy array or PIL image)

            Returns:
            image (numpy array or PIL image)

            Note: You do not need to resize the bounding boxes. ONLY RESIZE THE IMAGE.
        '''
        im = Image.open(image)
        im.show()
        print(f"{im.size}")
        if(isinstance(self.output_size, int)):
            a = im.size[0]
            b = im.size[1]
            c = self.output_size

            if(a > b):
                ratio = int(a/b)
                imim = im.resize((c*ratio, c))
            else:
                ratio = int(b/a)
                imim = im.resize((c, c*ratio))

            
        else:

            imim = im.resize((self.output_size[0], self.output_size[1]))

        return imim

# tu = (100, 100)
# image = RescaleImage(400)
# im = image.__call__('/home/datta/Desktop/index.jpeg')
# im.show()