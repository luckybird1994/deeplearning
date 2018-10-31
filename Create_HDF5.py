import h5py
import os
import sys
import cv2
import numpy as np

"""
路径说明: 

1.当前文件夹下，voc图片保存的位置。
2.当前文件夹下，分别保存train和val图片的big,small,middle大小文件。
"""

BASE_IMAGE_PATH = 'datasets/VOCdevkit/VOC2012/JPEGImages'
BASE_H5PY_PATH = 'datasets/h5py'
BASE_VOC_PATH = 'datasets/VOCdevkit/VOC2012'

#20个类图片的名称
LABELS = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable',
          'dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']


def load_image( image_path ):

    img = cv2.imread( image_path )
    img = cv2.resize( img, (256,128), interpolation=cv2.INTER_CUBIC )
    #print( img.shape )
    return img

def process_image(directory, name):

    image_path = os.path.join( directory,name+'.jpg')
    img = load_image( image_path )
    print(img.shape)
    return img

def create_voc_datasets( type = 'train', size = 'big' ):

    """
    :param type: 数据集的制作分成train和val
    :param size: 大小为big,middle,small. big为voc全部8815张图片; middle选取其中2000张; small选取10张，就是看一下效果罢了
    :return:
    """

    hdf5_path = os.path.join( BASE_H5PY_PATH,size,type,type + '.hdf5' )
    print( ">> hdf5_path", hdf5_path )
    hdf5_file = h5py.File( hdf5_path, mode='w' )
    name = 'image'
    num = 100

    if size == 'big':
        num = 8815
    elif size == 'middle':
        num = 2000
    elif size == 'small':
        num = 100

    train_shape = ( num, 128, 256,3 )
    hdf5_file.create_dataset( name, train_shape, np.uint8)
    label = 0
    k = 0

    while label <= 19:

        split = LABELS[label] + '_' + type
        label += 1
        split_file_path = os.path.join( BASE_VOC_PATH, 'ImageSets', 'Main', '%s.txt' % split )
        print('>> split_file_path:', split_file_path)
        with open( split_file_path ) as f:
            filenames = f.readlines()

        i = 0
        new_filenames = []
        while i < len(filenames):
            if filenames[i].find('-1') == -1:
                new_filenames.append(filenames[i])
            i = i + 1

        len_newfiles = len(new_filenames)
        len_newfiles = len_newfiles // 5 * 5

        if size == 'middle':
            len_newfiles = 100
        elif size == 'small':
            len_newfiles = 5

        j = 0
        while j < len_newfiles:

            sys.stdout.write('\r>> Converting image %d/%d' % (j + 1, len_newfiles))
            sys.stdout.flush()
            filename = new_filenames[j][0:11]
            img = process_image( directory = BASE_IMAGE_PATH , name = filename )
            hdf5_file[name][k, ...] = img[None]
            j += 1
            k += 1
        sys.stdout.flush()
    print(">> k", k)

