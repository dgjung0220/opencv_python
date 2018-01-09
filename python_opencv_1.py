import numpy as np
import cv2
from matplotlib import pyplot as plt

def ask_version() :
    # cv version
    print(cv2.__version__)

def Load_Image() :
    # Load an color image in grayscale
    img = cv2.imread('./test_image/kermit000.jpg', 0)

    # display an image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)       # default : WINDOW_AUTOSIZE     # cv2.WINDOW_NORMAL : 윈도우의 크기를 조정할 수 있다.
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def Write_Image() :
    img = cv2.imread('./test_image/kermit000.jpg', 0)
    cv2.imshow('image', img)
    keyboard = cv2.waitKey(0)

    # 키값을 이용하여 이미지 만들기
    if keyboard == 27 :             # ESC
        cv2.destroyAllWindows()
    elif keyboard == ord('s') :       # 's' key
        # Write a image
        cv2.imwrite('./test_image/kermit000_gray.jpg', img)
        cv2.destroyAllWindows()

def Use_Matplotlib_Image() :
    #matplotlib
    img = cv2.imread('./test_image/lena512.bmp', 0)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])
    plt.show()

def capture_video() :
    # Capture Video from Camera
    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame came here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break;

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def save_video_from_capture() :
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('./test_video/output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)

            cv2.imshow('frame',frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

