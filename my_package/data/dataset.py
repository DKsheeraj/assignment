#Imports
import jsonlines

from PIL import Image
import os
import numpy as np


class Dataset(object):
    '''
        A class for the dataset that will return data items as per the given index
    '''
    
    items = []
    def __init__(self, annotation_file, transforms=None):
        '''
            Arguments:
            annotation_file: path to the annotation file
            transforms: list of transforms (class instances)
                        For instance, [<class 'RandomCrop'>, <class 'Rotate'>]
        '''
        self.annotation_file = annotation_file
        self.transforms = transforms
        f = jsonlines.open(self.annotation_file)
        self.data = f
        #print(self.data)
        

    def __len__(self):
            '''
                return the number of data points in the dataset
            '''
            count =  0
            
            for line in self.data.iter():

                self.items.append(line)
             
                count += 1
                
            
            return count  

        

    
    def __getann__(self, idx):
        '''
            return the data items for the index idx as an object
        '''
        # items = []
        # with open(self.annotation_file, 'r') as file:
        #     content = file.read()
        # with jsonlines.Reader(content) as reader:
        #      #items = [op for op in reader]
        #     for op in reader:
        #         items.append(op)

        return self.items[idx]
        
        
        
        
       
        



    def __transformitem__(self, path):
        '''
            return transformed PIL Image object for the image in the given path
        '''
        
        image = Image.open(path)
        pth = path
        for classes in self.transforms:
            
            temp =  classes(pth)
            temp.save("/home/datta/Desktop/3.jpeg")
            pth = "/home/datta/Desktop/3.jpeg"
        
        return temp
        
            

#obj = Dataset('/home/datta/Desktop/annotations.jsonl')
# obj.__transformitem__("/home/datta/Desktop/index.jpeg")
# print(obj.__len__())
# print(obj.__getann__(1))
# print(obj.__getann__(2))


