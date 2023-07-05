# HAAR_CASCADE
    * 머신 러닝 기반의 오브젝트 탐지 알고리즘
    * 특징(feature) 기반으로 오디오 / 비디오에서 오브젝트 탐지
    * 직사각형 영역으로 구성되는 특징을 활용하기에 더 빠름

    ## 단계
        1. 특징 선택 (Haar Feature Selection)
            * 이미지 전체에서 하르 특징을 계산
                - 직사각형들의 영역 내의 픽셀의 합 차이를 계산
            * 하르 특징 값은 아래 이미지에서 검정 부분의 합에서 흰 부분 합을 뺀 값
            ![alt text](https://github.com/donghquinn/haar_face_detection/master/haar_feature_rectangle.png)