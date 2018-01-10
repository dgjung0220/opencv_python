import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('./test_image/ET/et000.jpg', 0)
img2 = cv2.imread('./test_image/ET/et008.jpg', 0)

# Initiate SIFT detecter
orb = cv2.ORB_create()

# computing descripter
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img1, None)

# matching descriptors # Brute-Force
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors
matches = bf.match(des1, des2)

# Sort them in order to their distance.
matches = sorted(matches, key=lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], img1, flags=2)
plt.imshow(img3)
plt.show()


def Use_BRISK() :
    img1 = cv2.imread('./test_image/ET/et000.jpg',0)
    # gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

    brisk = cv2.BRISK_create()
    # keypoint = brisk.detect(gray, None)
    keypoint = brisk.detect(img1, None)

    img = cv2.drawKeypoints(img1, keypoint, img1)
    plt.imshow(img)
    plt.show()