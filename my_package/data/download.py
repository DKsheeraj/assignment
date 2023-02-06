from PIL import Image
import requests

from io import BytesIO

class Download(object):
    '''
        A class for helping in dowloading the required images from the given url to the specified path
    '''

    def __call__(self, path, url):
        '''
            Arguments:
            path: download path with the file name
            url: required image URL
        '''
    
        img = Image.open(requests.get(url, stream = True).raw)
        img.save(path) 


# url = 'http://farm5.staticflickr.com/4127/5172389204_31214fdc50_z.jpg'
# path = '/home/datta/Desktop/mayukha2.jpg'
# img = Download()
# img.__call__(path, url)