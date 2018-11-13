import cv2
import tensorflow as tf
import tensorflow.contrib.eager as tfe
tfe.enable_eager_execution()
import numpy as np

#Weighted Structural Loss
#paper link: https://arxiv.org/pdf/1802.06527.pdf

labels = [ [ 0,0], [0,1] ]
#logits = [ [2,0.5], [0.1, 0] ]
logits = np.zeros( (2,2,2), dtype=np.float32 )
logits[:,:,0 ] = 1.233333
logits[:,:,1] = 2.233333

logits_scaled = tf.nn.softmax( logits )
print( logits_scaled )
result = -tf.reduce_sum( labels * tf.log(logits_scaled), 1 )
result1 = tf.nn.softmax_cross_entropy_with_logits( labels=labels, logits=logits)
print( result )
print( result1 )