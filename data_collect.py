import cv2
import pytesseract
import numpy as np
from matplotlib import pyplot as plt

##데이터 ROI 저장
img_metal_type=cv2.imread('metal_type.png')
img_wattage_temp=cv2.imread('wattage.png', cv2.IMREAD_GRAYSCALE)
img_meter_detail=cv2.imread('meter_detail.png')
img_model_name=cv2.imread('model_name.png')
img_serial_number=cv2.imread('serial_number.png')

##img_wattage 인식 개선을 위한 경계선 처리
'''median_intensity = np.median(img_wattage_temp) # 픽셀 강도의 중간값을 계산

lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))

img_wattage = cv2.Canny(img_wattage_temp, lower_threshold, upper_threshold)'''

##img_wattage 인식 개선을 위한 threshold 이진화
img_wattage=cv2.adaptiveThreshold(img_wattage_temp,400,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,99,10)
cv2.imshow('img', img_wattage)
cv2.waitKey()
cv2.destroyAllWindows()
##데이터 읽기
#설정
config = ('-l kor+eng --oem 3 --psm 4')

print(pytesseract.image_to_string(img_wattage,config=config))
