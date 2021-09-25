import cv2
##드래그로 데이터 ROI 추출

list=['metal_type.png','wattage.png','meter_detail.png','model_name.png','serial_number.png']
temp=1 #list 에서 저장명 선택 후 출력

isDragging = False
x0, y0, w, h = -1, -1, -1, -1
blue, red = (255, 0, 0), (0, 0, 255)
 
def onMouse(event, x, y, flags, param):
    global isDragging, x0, y0, img
    if event == cv2.EVENT_LBUTTONDOWN:
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x - x0
            h = y - y0
            if w > 0 and h > 0:
                img_draw = img.copy()
                cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
                cv2.imshow('img', img_draw)
                roi = img[y0:y0+h, x0:x0+w]
                cv2.imshow('cropped', roi)
                cv2.moveWindow('cropped', 0, 0)
                cv2.imwrite(list[temp], roi)
            else:
                cv2.imshow('img', img)
                print('왼쪽 상단부터 우측 하단으로 드래그 하세요.')
 
#음영처리하며 불러오기
img = cv2.imread('C:/Users/Lee/project_lfin/shape_ROI_test.png',cv2.IMREAD_GRAYSCALE)
#원본출력
cv2.imshow('img', img)
#함수호출
cv2.setMouseCallback('img', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()