import numpy as np
import cv2

def drawing_line(img) :
    # Draw a diagonal blue line with thickness of 5 px
    img = cv2.line(img, (0,0), (511,511), (255,0,0),5)
def drawing_rect(img) :
    img = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)  # 3 px, green rect.
def drawing_circle(img) :
    img = cv2.circle(img, (447,63), 63, (0,0,255), -1)          # red, -1 은 fill inside
def drawing_ellipse(img) :
    img = cv2.ellipse(img, (256,256), (100,100),0,0, 180, 255, -1)
def drawing_polygon(img) :
    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
    pts = pts.reshape((-1,1,2))
    img = cv2.polylines(img, [pts], True, (0,255,255))


# Create a black image
img = np.zeros((512, 512,3), np.uint8)

drawing_polygon(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()