import h5py
import os
import cv2
import numpy as np



def create_voc_datasets():


    hdf5_path = os.path.join( "please write the path where you want save your hdf5 file")
    hdf5_file = h5py.File( hdf5_path, mode='w' )

    name = 'image' # this is like the key in dictionary, you need this to find value
    num = 100 # the size of hdf5 file, in other words, this is the number of image you want to save in hdf5 file.you can change!

    train_shape = ( num, 128, 256,3 ) # ( 128,256,3 ) is the shape of image, like W*H*C.

    hdf5_file.create_dataset( name, train_shape, np.uint8 )

    for i in range( num ):

        image_path = "you may write your image file path"
        img = cv2.imread( image_path ) # you can also pre_process your image as you like, but the shape will be like( 128,256,3 )
        hdf5_file[name][i,...] = img[None]





