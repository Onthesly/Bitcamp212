import cv2

image = cv2.imread('./ch04/read_color.jpg', cv2.IMREAD_COLOR)
if image is None: raise Exception('영상파일 읽기 에러')             # 예외처리

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10)                     # JPEG 화질 설정
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9]                   # PNG 압축 레벨 설정

## 행렬을 영상파일로 저장
cv2.imwrite('./ch04/write_test1.jpg', image)                    # 디폴트는 95
cv2.imwrite('./ch04/write_test2.jpg', image, params_jpg)        # 지정한 화질로 저장
cv2.imwrite('./ch04/write_test3.png', image, params_png)
cv2.imwrite('./ch04/write_test4.bmp', image)                    # BMP 파일로 저장
print('저장 완료')