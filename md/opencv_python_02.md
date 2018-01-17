### Video reading & writing

#### Capture video from camera(webcam)
웹캠을 이용하여 영상을 흑백으로 변환하고 'q' 가 입력되면 종료되는 코드를 아래와 같이 작성한다.
```python
import cv2

def capture_video() :
    cap = cv2.VideoCapture(0)                               # 비디오 캡처를 위한 'cap' 객체

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
    cap.release()                                           # cap 객체 해제 (release)
    cv2.destroyAllWindows()
```
``ret, frame = cap.read()``, 재생되는 비디오의 한 프레임씩 읽는다. 성공/실패에 따라 ret 값은 true/false 를 반환한다.  
cap 객체는 제대로 초기화되지 않는 경우가 있는데, 이 경우 에러 코드를 리턴한다. ``cap.isOpened()`` 를 이용하여 cap 의 초기화 상태를 확인할 수 있다. 만약 false이면 ``cap.open()``을 사용하여 연다.
비디오 프레임의 폭과 높이를 알고 싶다면, ``cap.get(3) , cap.get(4)`` 를 이용하고, 새롭게 폭,높이를 설정하려면 아래와 같이 사용한다.
```python
# 640 x 480 프레임 사이즈 설정
ret = cap.set(3, 640)
ret = cap.set(4, 480)
```

#### Save Video
아래 코드는 웹캠화면을 DIVX 코덱을 적용하여 초당 프레임 수 20 (사이즈 640*480)으로 비디오를 저장하며, 'q' 버튼을 누르면 종료한다.
```python
import cv2

def save_video_from_capture() :
    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object

    fourcc = cv2.VideoWriter_fourcc(*'XVID')                                    # fourcc = cv2.VideoWriter_fourcc('D','I','V','X')
    out = cv2.VideoWriter('./test_video/output.avi',fourcc, 20.0, (640,480))

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,0)                                           # flip 화면 거꾸로 출력.

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
``` 
``out = cv2.VideoWriter('./test_video/output.avi',fourcc, 20.0, (640,480))``, 비디오 저장을 위한 out 객체
