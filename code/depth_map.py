import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('./test_image/left.jpg', 0)
img2 = cv2.imread('./test_image/right.jpg', 0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(img1, img2)

plt.xticks([]), plt.yticks([])
plt.imshow(disparity, 'gray')
plt.show()