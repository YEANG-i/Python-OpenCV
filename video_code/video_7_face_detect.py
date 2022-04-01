import time

import cv2 as cv

video = 'video/hand_2.mp4'
video_deal_out = 'video/video_deal_out.avi'

pTime = 0
cTime = 0

# 1.读取摄像头
cap = cv.VideoCapture(0)
# 2.在每一帧数据中进行人脸检测
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # 3.实例化OpenCV人脸识别的分类器
        face_cas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
        face_cas.load('haarcascade_frontalface_default.xml')
        # 4.调用识别人脸
        faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(32, 32))
        for faceRect in faceRects:
            x, y, w, h = faceRect
            # 框出人脸
            cv.rectangle(frame, (x, y), (x + h, y + w), (0, 255, 0), 3)

        # FPS
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        print('FPS:{:.0f}'.format(fps))
        cv.putText(frame, 'FPS:{:.0f}'.format(fps), (30, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 5)
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == 27:
            break
# 5. 释放资源
cap.release()
cv.destroyAllWindows()
