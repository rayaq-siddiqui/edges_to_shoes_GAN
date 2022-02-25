'''
Rayaq Siddiqui
We are going to be splitting the data from the sketches and the handbag into two different images

This way we can have a seperation in Domain A and Domain B
'''

# Data Science Libraries
import numpy as np
import os
from cv2 import imread, imwrite
from elapsedtimer import ElapsedTimer
import shutil


'''
def process_data(path, _dir_):
    os.chdir(path)
    try:
        os.makedirs('valA')
    except:
        print(f'Folder valA already present, cleaning up and recreating empty folder valA')
        try:
            os.rmdir('valA')
        except:
            shutil.rmtree('valA')

        os.makedirs('valA')

    try:
        os.makedirs('valB')
    except:
        print(f'Folder valB already present, cleaning up and recreating empty folder valB')
        try:
            os.rmdir('valB')
        except:
            shutil.rmtree('valB')

        os.makedirs('valB')

    os.chdir('../')
    files = os.listdir(path + _dir_ )
    print('Images to process:', len(files))

    i = 0
    for f in files:
        i += 1
        img = imread(path + _dir_ + str(f))
        w,h,d = img.shape
        h_ = int(h/2)
        img_A = img[:,:h_]
        img_B = img[:,h_:]

        imwrite(f'{path}/valA/{str(f)}_A.jpg', img_A)
        imwrite(f'{path}/valB/{str(f)}_B.jpg', img_B)

        if ((i % 10000) == 0 & (i >= 10000)):
            print(f'the number of input images processed : {i}')

    files_A = os.listdir(path + 'valA/')
    files_B = os.listdir(path + 'valB/')
    print(f'No of images written to {path}/valA is {len(files_A)}')
    print(f'No of images written to {path}/valA is {len(files_B)}')


with ElapsedTimer('process Domain A and Domain B Images'):
    process_data('data/', 'val/')
'''