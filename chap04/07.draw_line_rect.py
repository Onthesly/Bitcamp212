import numpy as np
import cv2

blue, green, red = (255,0,0), (0,255,0), (0,0,255)              # 색상 선언
image = np.zeros((400,600,3), np.uint8)                         # 3채널 컬러 영상 생성
image[:] = (255,255,255)                                        # 3채널 흰색

pt1, pt2 = (50,50), (250,150)                                   # 좌표 선언 - 정수형 튜플
pt3, pt4 = (400,150), (500,50)
roi = (50,200,200,100)                                          # 사각형 영역 - 4원소 튜플

## 직선 그리기
cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)                # 계단 현상 감소선

## 사각형 그리기
cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)             # 4방향 연결선
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)                   # 8방향 연결선
cv2.rectangle(image, (400,200,100,100), green, cv2.FILLED)      # 내부 채움

cv2.imshow('Line & Rectangle', image)                           # 윈도우에 영상 표시
cv2.waitKey()
cv2.destroyAllWindows()                                         # 모든 열린 윈도우 닫기