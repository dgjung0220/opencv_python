import cv2
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('../test_image/opengl_cover.jpg', 0)
frame = cv2.imread('../test_image/book_covers.jpg',0)

# orb = cv2.ORB_create(scoreType=cv2.ORB_FAST_SCORE)
# orb = cv2.ORB_create(nfeatures=100000, scoreType=cv2.ORB_FAST_SCORE)
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

kp, desc = orb.detectAndCompute(img, None)
img = cv2.drawKeypoints(img, kp, None)
target_feature_num = len(kp)
print(target_feature_num)

frame_kp, frame_desc = orb.detectAndCompute(frame, None)
frame = cv2.drawKeypoints(frame, frame_kp, None)

matches = bf.match(desc, frame_desc)
matches = sorted(matches, key=lambda x:x.distance)

min_dist = matches[0].distance
max_dist = matches[len(matches)-1].distance

good_matches = []
obj = []
scene = []

for i in range(0, len(matches)):
    if matches[i].distance < 2.5 * min_dist :
         good_matches.append(matches[i])

output = cv2.drawMatches(img, kp, frame, frame_kp, good_matches, None, flags=2)

for i in range(0, len(good_matches)) :
    obj.append(kp[good_matches[i].queryIdx].pt)
    scene.append(kp[good_matches[i].queryIdx].pt)

obj = np.array(obj, np.float32)
scene = np.array(scene, np.float32)

H = cv2.findHomography(obj, scene, cv2.FM_RANSAC)

obj_corner = []
obj_corner.append([0,0])
obj_corner.append([img.shape[1], 0])
obj_corner.append([img.shape[1], img.shape[0]])
obj_corner.append([0,img.shape[0]])
obj_corner = np.array(obj_corner, dtype='float32')

scene_corner = cv2.perspectiveTransform(obj_corner, H)

# cv2.line(output, scene_corner[0] + [output.shape[1], 0], scene_corner[1] + [output.shape[1], 0], np.ScalarType(0,255,0), 4)







# plt.subplot(221)
# plt.imshow(img)
#
# plt.subplot(222)
# plt.imshow(frame)
#
# plt.subplot(212)
# plt.imshow(output)
#
# plt.imshow(output)
# plt.show()



# # bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# flann = cv2.FlannBasedMatcher(cv2.NORM_HAMMING)
#
# target = cv2.imread('../test_image/lg-g5.jpg')
# target_kp, target_des = orb.detectAndCompute(target, None)
#
# while (True):
#     # Capture frame-by-frame
#     ret, frame = cap.read()
#
#     kp, des = orb.detectAndCompute(frame, None)
#
#     matches = flann.match(des, target_des)
#     # matches = sorted(matches, key=lambda x:x.distance)
#
#     result_frame = cv2.drawMatches(frame, kp, target, target_kp, matches[:300], None, flags=2)
#
#     # Display the resulting frame
#     cv2.imshow('result_frame', result_frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break;