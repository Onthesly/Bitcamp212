import cv2
from Common.utils import put_string


def zoom_bar(value):                                            # 줌 조절 콜백 함수
    global capture
    capture.set(cv2.CAP_PROP_ZOOM, value)                       # 줌 설정


def focus_bar(value):                                           # 초점조절 콜백 함수
    global capture
    capture.set(cv2.CAP_PROP_FOCUS, value)


capture = cv2.VideoCapture(0)                                   # 0번 카메라 연결
if capture.isOpened() == False: raise Exception('카메라 연결 안됨')    # 예외처리

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 400)                      # 카메라 프레임 너비
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)                     # 카메라 프레임 높이
capture.set(cv2.CAP_PROP_AUTOFOCUS, 0)                          # 자동초점 중지
capture.set(cv2.CAP_PROP_BRIGHTNESS, 100)                       # 프레임 밝기 초기화

title = 'Change Camera Properties'                              # 윈도우 이름 지정
cv2.namedWindow(title)                                          # 윈도우 생성
cv2.createTrackbar('zoom', title, 0, 10, zoom_bar)              # 줌 트랙바
cv2.createTrackbar('focus', title, 0, 40, focus_bar)            # 포커스 트랙바

while True:
    ret, frame = capture.read()                                 # 카메라 영상 받기
    if not ret: break
    if cv2.waitKey(30) >= 0: break

    zoom = int(capture.get(cv2.CAP_PROP_ZOOM))                  # 카메라 속성 가져오기
    focus = int(capture.get(cv2.CAP_PROP_FOCUS))
    put_string(frame, 'zoom : ', (10,240), zoom)                # 줌 값 표시
    put_string(frame, 'focus : ', (10,270), focus)              # 초점 값 표시
    cv2.imshow(title, frame)

capture.release()                                               # 비디오 캡쳐 메모리 해제
