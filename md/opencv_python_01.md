### Image reading & writing

#### Load Image
```python
import numpy as np
import cv2

def Load_Image() :
    # Load an color image in grayscale
    img = cv2.imread('./test_image/kermit000.jpg', cv2.IMREAD_COLOR)

    # display an image
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

``img = cv2.imread('./test_image/kermit000.jpg', cv2.IMREAD_COLOR)`` , opencv 의 imread 함수는 이미지 파일을 읽기 위한 객체를 리턴한다. 첫 번째 인자는 읽고자 하는 이미지 파일 경로, 두 번쨰 인자는 이미지 파일을
읽는 방식을 나타내는 플래그이다.  
- cv2.IMREAD_COLOR : 컬러 이미지로 로드함.
- cv2.IMREAD_GRAYSCALE : 흑백 이미지로 로드함. 정수값 0
- cv2.IMREAD_UNCHANGED : 알파채널(Alpha-Channel)을 포함하여 이미지 그대로 로드람. 정수값 -1  

``cv2.imshow('image', img)``, cv2.imread() 에 의해 반환된 이미지 객체 img를 화면에 나타내기 위한 함수. 첫 번째 인자는 윈도우의 타이틀, 두 번쨰 인자는 화면에 표시할 이미지 객체.  
 ``cv2.waitKey(0)`` 는 화면에 이미지를 표시한 후 사용자가 키보드를 누를 때까지 대기하라는 코드이다. 인자는 키보드 입력을 기다리는 시간으로 1/1000 초 (ms) 단위로 입력된다. 함수의 리턴값은 사용자가 누른 키보드 값이다.
 
 #### cv2.waitKey() 반환값 이용
 ``cv2.waitKey()``의 반환값을 이용하여 's' 를 입력하면 이미지를 저장하는 함수를 아래와 같이 작성할 수 있다.
 ```python
import numpy as np
import cv2

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

```

#### Matplotlib 을 이용한 Image read
`Matplotlib` 은 파이썬을 위한 플로팅 라이브러로써 광범위하고 다양한 floating 연산 method를 제공한다.
결과를 보면 이미지 Zoom, 저장 등 다양한 기능을 사용할 수 있다.
```python
import numpy as np
import cv2
from matplotlib import pyplot as plt

def Use_Matplotlib_Image() :
    #matplotlib
    img = cv2.imread('./test_image/lena512.bmp', 0)
    plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
    plt.xticks([]), plt.yticks([])                              # x, y축 눈금 표시
    plt.show()
```
※ OpenCV는 BGR 모드로 컬러 이미지를 다루지만, Matplotlib 은 RGB 모드로 컬러 이미지를 다룬다. 그래서 OpenCV로 읽어들인 컬러 이미지 객체를 matplotlib 에서 그대로 사용할 경우, 색상이 제대로 나타나지 않는 문제점이 있다.