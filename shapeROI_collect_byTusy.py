import cv2
import numpy as np
from matplotlib import pyplot as plt
#==========================형태 ROI 추출============================#
##파일읽기
img = cv2.imread('C:/Users/Lee/project_lfin/images/IOS_image.jpg')

##투시변환
# [x,y] 좌표점을 4x2의 행렬로 작성
# a=좌상 b=좌하 c=우상 d=우하
ax=160;ay=1000
bx=155;by=3230
cx=2650;cy=960
dx=2710;dy=3230
pts1 = np.float32([[ax,ay],[bx, by],[cx,cy],[dx,dy]])

# 좌표의 이동점
pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (ax,ay), 20, (255,0,0),-1)
cv2.circle(img, (bx,by), 20, (0,255,0),-1)
cv2.circle(img, (cx,cy), 20, (0,0,255),-1)
cv2.circle(img, (dx,dy), 20, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

#1000*1000 사이즈로 지정
shaped_ROI = cv2.warpPerspective(img, M, (1000, 1000))

##형태ROI 저장
cv2.imwrite('shape_ROI_test.png',shaped_ROI)

##출력
#plt.subplot(121),plt.imshow(img),plt.title('image')
#plt.subplot(122),plt.imshow(shaped_ROI),plt.title('Perspective')
#plt.show()

#==========================데이터 ROI 추출============================#
###드래깅을 이용한 데이터 추출
##드래깅 함수
#저장할 데이터ROI의 이름을 입력(설정값)




