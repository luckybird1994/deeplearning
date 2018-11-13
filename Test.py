# this file is test something that i cannot confirm

import cv2
import numpy as np

img = cv2.imread( "201771.jpg" )
print( img[None].shape )
print( img.shape )

num = [[],[],[],[],[],[]]

num = np.array( [[0,1,2],[2,1,3]] )
print( np.sum(num, axis=-1) )
print( np.sum(num, axis=1) )

num = np.zeros( (1,1,2), dtype=np.int32 )
num[0,0,1] = 1

print( np.sum( num, axis = 1) )
print( np.sum( num, axis = -1) )