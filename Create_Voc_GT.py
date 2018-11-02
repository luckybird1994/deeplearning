import cv2
import numpy as np

LABEL_ARRAYS = np.array( [ [ [128,0,0],[0,128,0],[128,128,0],[0,0,128],[128,0,128], [0,128,128],[128,128,128],
                             [64,0,0],[192,0,0],[64,128,0],[192,128,0],[64,0,128],[192,0,128],[64,128,128],[192,128,128],
                             [0,64,0],[128,64,0],[0,192,0],[128,192,0],[0,64,128]  ]],dtype=np.uint8)

LABELS = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable',
          'dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']

label = 0

for label in range( 20 ):

    classes = LABELS[label]
    num = 0
    tot_class_num = 100 # the tot num of this class

    for num in range( tot_class_num ):
        img = cv2.imread("the path you save class **** gt images")  # if label = 0, and you will process aeroplane images
        w,h,c = img.shape

        #attention: cv2.imread is bgr image
        for i in range( w ):
            for j in range( h ):
                if img[i, j, 2] == LABEL_ARRAYS[0, label, 0] and img[i, j, 1] == LABEL_ARRAYS[0, label, 1] and img[i, j, 0] == LABEL_ARRAYS[0, label, 2]:
                    img[i, j, 0] = 255
                    img[i, j, 1] = 255
                    img[i, j, 2] = 255
        cv2.imwrite( " the path you want to save your file", img )


