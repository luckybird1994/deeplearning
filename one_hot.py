import numpy as np
import cv2


def one_hot_it(label, label_values):

    """
    Convert a segmentation image label array to one-hot format
    by replacing each pixel value with a vector of length num_classes

    # Arguments
        label: The 2D array segmentation image label
        label_values

    # Returns
        A 2D array with the same width and hieght as the input, but
        with a depth size of num_classes
    """

    # https://stackoverflow.com/questions/46903885/map-rgb-semantic-maps-to-one-hot-encodings-and-vice-versa-in-tensorflow
    # https://stackoverflow.com/questions/14859458/how-to-check-if-all-values-in-the-columns-of-a-numpy-matrix-are-the-same
    semantic_map = []
    for colour in label_values: #先找所有的[0,0,0],再找所有的[ 255,255,255 ]
        equality = np.equal(label, colour)
        print( "---",equality.shape )
        class_map = np.all(equality, axis=-1) #最后一个通道
        print( "!!!",class_map.shape  )
        semantic_map.append(class_map)

    semantic_map = np.stack(semantic_map, axis=-1)

    return semantic_map

label_values = [ [0,0,0], [255,255,255] ]

output_image = cv2.imread( "gt.bmp" )
#output_image = np.zeros( (2,2), dtype=)
print( output_image.shape )
label = one_hot_it( output_image, label_values )