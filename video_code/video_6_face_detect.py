import time

import cv2 as cv

video = 'video/hand_2.mp4'
video_deal_out = 'video/video_deal_out.avi'

pTime = 0
cTime = 0

# 1.读取视频
cap = cv.VideoCapture(0)
retval_width = cap.get(3)  # 获取视频的宽高
retval_height = cap.get(4)  # 获取视频的宽高
retval_fps = cap.get(5)  # 获取视频的FPS
print('Video_width:{:.0f}\nVideo_height:{:.0f}\nVideo_FPS:{:.0f}\n'
      .format(retval_width, retval_height, retval_fps))

# 视频写入
retval_out = cv.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 设置视频编码格式
out = cv.VideoWriter(video_deal_out, retval_out, 30, (int(retval_width), int(retval_height)))

# 2.在每一帧数据中进行人脸识别
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

        out.write(frame)  # 将每一帧写入文件
        print("1")
        cv.imshow("frame", frame)
        if cv.waitKey(1) & 0xFF == 27:
            break
# 5. 释放资源
cap.release()
out.release()  # 释放写的资源
cv.destroyAllWindows()
