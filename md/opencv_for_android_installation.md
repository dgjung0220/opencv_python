###OpenCV For Android Installation

#### 1. Download
[OpenCV.org](https://opencv.org/releases.html) 에서 최신 버전의 Opencv SDK for android 다운로드 후 압축 해제.

#### 2. Import OpenCV to Android Studio
File > New > Import Module > 압축 해제한 폴더의 하위 sdk>java 폴더 선택

#### 3. Update build.gradle
아래 하위 4개의 필드가 OpenCV SDK Version에 맞도록 업데이트. (Install missing platform & sync project)

1. compileSdkVersion
2. buildToolVersion
3. minSdkVersion
4. targetSdkVersion

#### 4. Module dependency 추가
Project Structure(Ctrl+Alt+shift+S) > app > Modules > Dependencies > '+' 버튼 클릭 후, 3 Module dependency 선택하여 OpenCV 추가.  
import org.opencv 가 자동 완성되는지 확인.

#### 정적 라이브러리 추가
New > Directory > jniLibs 생성 > jniLibs 내부에 openCV-X.X.X*/sdk/native/libs 의 내용을 복사