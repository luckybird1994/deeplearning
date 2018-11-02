This project contain things that i encounter when i learn DL

Create_HDF5.py:
this file tell you how to create and load hdf5 data file

Create_Voc_GT.py
sometimes, you want to use only black and white Ground Truth images in Voc2012 GT.
However, they only provide ground truth with blue,red, and yellow colors, etc.
so, this file tell you how to create black and white Voc ground truth.
first, wo need to know that how original GT images( offical GT images ) work.
you should know the voc datasets contain 20 class image, and each class has its corresponding rgb value

LABEL_ARRAYS = np.array( [ [ [128,0,0],[0,128,0],[128,128,0],[0,0,128],[128,0,128], [0,128,128],[128,128,128],
                             [64,0,0],[192,0,0],[64,128,0],[192,128,0],[64,0,128],[192,0,128],[64,128,128],[192,128,128],
                             [0,64,0],[128,64,0],[0,192,0],[128,192,0],[0,64,128]  ]],dtype=np.uint8)

LABELS = ['aeroplane','bicycle','bird','boat','bottle','bus','car','cat','chair','cow','diningtable',
          'dog','horse','motorbike','person','pottedplant','sheep','sofa','train','tvmonitor']

for examples, class "aeroplane", and its rgb value is [128,0,0]; class "bicycle", and its rgb values is [0,128,0], etc....
so, we can write the code...
