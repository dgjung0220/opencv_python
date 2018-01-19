### 이미지 픽셀 조작 및 ROI 설정

#### cv2 이미지 픽셀 조작

```python
import cv2

def default() :
    img = cv2.imread('../test_image/ET/et000.jpg')
    px = img[340, 200]                                    # 340, 200 픽셀값 반환
    print(px)                                             # [35 35 35]
    img[340, 200] = [0, 0, 0]                             # 픽셀값을 (0,0,0) 검은 색으로 변환
```