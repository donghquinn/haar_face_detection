import cv2

def haarFaceDetection():
    """
        XML 포맷의 분류기 코드
        - frontalface: 정면
        - eye: 눈
    """
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # 카메라 선택
    vid = cv2.VideoCapture(1)

    while True:
        # 카메라 구동
        ret, frame = vid.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        """
            gray         : 분석될 이미지 또는 영상 프레임
            scaleFactor  :  이미지에서 얼굴 크기가 서로 다른 것을 보상해주는값 
            minNeighbors : 얼굴 사이의 최소 간격( 픽셀 ) 
            minSize      : 얼굴의 최소 크기
        """
        faces = face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize=(30,30))

        # 얼굴 좌표 선택
        for (x,y,w,h) in faces:
                # 얼굴 좌표를 받아 사각형으로 표시
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

                """
                    ROI: Regin of Interst. 관심영역. 
                    즉 영상 내에서 관심 있는 영역 설정
                """
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                # 눈 탐지
                eyes = eye_cascade.detectMultiScale(roi_gray)

                # 눈 좌표값 받기
                for (ex,ey,ew,eh) in eyes:
                    # 받아온 눈 좌표를 사각형으로 표시
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        # 이미지 표현
        cv2.imshow('View', frame)
        
        # q를 누르면 카메라 동작 정지
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # 카메라 객체 해제
    vid.release()

    # 창 종료
    cv2.destroyAllWindows()

haarFaceDetection()