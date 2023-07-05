# HAAR_CASCADE
    * [openCV Cascade](https://github.com/opencv/opencv/tree/master/data/haarcascades)
    
    * 머신 러닝 기반의 오브젝트 탐지 알고리즘
    * 특징(feature) 기반으로 오디오 / 비디오에서 오브젝트 탐지
    * 직사각형 영역으로 구성되는 특징을 활용하기에 더 빠름

    ## 단계
        1. 특징 선택 (Haar Feature Selection)
            * 이미지 전체에서 하르 특징을 계산
                - 직사각형들의 영역 내의 픽셀의 합 차이를 계산
            * 하르 특징 값은 아래 이미지에서 검정 부분의 합에서 흰 부분 합을 뺀 값

            ![alt text](https://github.com/donghquinn/haar_face_detection/blob/master/haar_feature_rectangle.png?raw=true)
        
        2. 적분 이미지 생성 (Integral Images)
            * 기존 이미지 너비와 높이에 1씩 더해 더 큰 이미지 생성 (= 적분 이미지 생성)
            * 맨 왼쪽과 위쪽은 0 으로 채움
            * 기존 이미지에 영역 지정하여 내부 값들의 합을 구함
            * 적분 이미지에서 원본에 지정한 영역의 오랜쪽 아래(대각선 아래) 픽셀에 대응하는 위치에 합 입력.

            ![alt text](https://github.com/donghquinn/haar_face_detection/blob/master/integral_images.png?raw=true)

