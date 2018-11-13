import cv2
import os


name = "cosal"
images = []
for file in os.listdir( "cosal/" ):
    images.append( file )

for file in images:
    filename = "cosal/" + file + '\n'
    with open( "cosal.txt", "a") as f:
        f.write( filename )

"""
folders = []

for fold in os.walk( "/Users/tanglv/SOD/SOD_Datasets/all/image/"):
    folders.append( fold )

len1 = len(folders[0][1])
i = 0

for i in range( len1 ):

    fold = folders[0][1][i]
    print( fold )
    for file in os.listdir( "/Users/tanglv/SOD/SOD_Datasets/all/image/" + fold + "/"):
        if file.find('.jpg') == -1:
            continue
        image_name = "/Users/tanglv/SOD/SOD_Datasets/all/image/" + fold + "/" + file
        img = cv2.imread( image_name )
        cv2.imwrite( "cosal/"+file,img)
    
"""

"""
folders = []

for fold in os.walk( "/Users/tanglv/SOD/SOD_Datasets/iCoseg/dataset_public/images/"):
    folders.append( fold )

len1 = len(folders[0][1])
i = 0
print( folders[0][1][0])

for i in range( len1 ):

    fold = folders[0][1][i]
    print( fold )
    for file in os.listdir( "/Users/tanglv/SOD/SOD_Datasets/iCoseg/dataset_public/images/" + fold + "/"):
        if file.find('.jpg') == -1:
            continue
        image_name = "/Users/tanglv/SOD/SOD_Datasets/iCoseg/dataset_public/images/" + fold + "/" + file
        img = cv2.imread( image_name )
        cv2.imwrite( "icoseg/"+file,img)
"""
