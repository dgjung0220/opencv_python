import numpy as np
import cv2

def default() :
    img = cv2.imread('../test_image/ET/et000.jpg')
    px = img[340, 200]                                    # 340, 200 픽셀값 반환
    print(px)                                             # [35 35 35]
    img[340, 200] = [0, 0, 0]                             # 픽셀값을 (0,0,0) 검은 색으로 변환

def use_numpy() :
    img = cv2.imread('../test_image/ET/et000.jpg')

    B = img.item(340,200, 0)
    G = img.item(340, 200, 1)
    R = img.item(340, 200, 2)

    BGR = [B, G, R]
    print(BGR)                                              # [35 35 35]

    # (340,200) 위치의 B 값을 100 으로 변경 (itemset)
    img.itemset((340, 200, 0), 100)
    print(img[340,200])                                     # [100 35 35]

def get_attribute() :
    img = cv2.imread('../test_image/ET/et000.jpg')

    print(img.shape)                                        # (480, 640, 3)
    print(img.size)                                         # 921600
    print(img.dtype)                                        # uint8

def ROI_1() :
    img = cv2.imread('../test_image/ET/et000.jpg')
    cv2.imshow('original', img)

    subimg = img[300:400, 350:640]
    cv2.imshow('ROI1', subimg)

    img[300:400, 0:290] = subimg

    print(img.shape)                                        # (480, 640, 3)
    print(subimg.shape)                                     # (100, 290, 3)

    cv2.imshow('modified', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def split_channel() :
    img = cv2.imread('../test_image/ET/et000.jpg')
    b, g, r = cv2.split(img)
    print(img[100, 100])                                # [86 75 91]
    print(b[100, 100], g[100,100], r[100, 100])         # 86 75 91

