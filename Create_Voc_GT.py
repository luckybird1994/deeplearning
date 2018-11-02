import os
import sys
import cv2
import numpy as np

SAVE_VOC_GT_IMAGE_PATH = 'datasets/VOCGT/image'
BASE_GT_PATH = 'datasets/VOCdevkit/VOC2012/SegmentationClass'
BASE_VOC_GT_TXT_PATH = 'datasets/VOCGT/txt'

LABEL_ARRAYS = np.array( [ [ [128,0,0],[0,128,0],[128,128,0],[0,0,128],[128,0,128], [0,128,128],[128,128,128],
                             [64,0,0],[192,0,0],[64,128,0],[192,128,0],[64,0,128],[192,0,128],[64,128,128],[192,128,128],
                             [0,64,0],[128,64,0],[0,192,0],[128,192,0],[0,64,128]  ]],dtype=np.uint8)

LABELS = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable',
          'dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']

def ground_truth( new_filenames, len_newfiles,k,label,type):

    z = 0
    folder = os.path.join(SAVE_VOC_GT_IMAGE_PATH, type, LABELS[label])
    os.makedirs(folder)
    while z < len_newfiles:

        new_gt_array = np.zeros( (128, 258, 3), dtype=np.uint8 )
        filename = new_filenames[z][0:11]

        gt_image_path = os.path.join(BASE_GT_PATH, filename + '.png')
        print('\n>>gt_image_path', gt_image_path)

        img = cv2.imread( gt_image_path, cv2.IMREAD_COLOR )
        img = cv2.resize(img, (256, 128), interpolation=cv2.INTER_AREA)
        for i in range(128):
            for j in range(256):
                if img[i, j, 2] == LABEL_ARRAYS[0,label,0] and img[i, j, 1] == LABEL_ARRAYS[0,label,1] and img[i, j, 0] == LABEL_ARRAYS[0,label,2]:
                    new_gt_array[i, j, 0] = 255
                    new_gt_array[i, j, 1] = 255
                    new_gt_array[i, j, 2] = 255

        save_name = os.path.join( SAVE_VOC_GT_IMAGE_PATH, type,LABELS[label],filename + '.png')
        cv2.imwrite( save_name,new_gt_array )
        k += 1
        z += 1

    return k

def create_ground_truth( type = 'train' ):

    label = 0
    k = 0

    while label <= 19:

        split = LABELS[label]

        split_file_path = os.path.join( BASE_VOC_GT_TXT_PATH,type,split +'.txt' )
        print( ">> split_file_path", split_file_path )

        with open(split_file_path) as f:
            filenames = f.readlines()


        k = ground_truth( new_filenames = filenames, len_newfiles = len(filenames) ,k = k,label=label,type = type )
        print( "%dFinshed" % label )
        label += 1
    print(">> k", k)
    return

