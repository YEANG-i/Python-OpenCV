import cv2 as cv


video_man = 'video/hand_1.mp4'
video_out = 'video/video_out.avi'


def main():
    cap = cv.VideoCapture(video_man)  # 读取视频
    retval_width = cap.get(3)  # 获取视频的宽高
    retval_height = cap.get(4)  # 获取视频的宽高
    retval_fps = cap.get(5)  # 获取视频的FPS
    print('Video_width:{:.0f}\nVideo_height:{:.0f}\nVideo_FPS:{:.0f}\n'
          .format(retval_width, retval_height, retval_fps))

    #
    retval_out = cv.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 设置视频编码格式
    out = cv.VideoWriter(video_out, retval_out, 30, (int(retval_width), int(retval_height)))

    while cap.isOpened():

        # display
        ret, frame = cap.read()
        if ret:
            cv.namedWindow('win_name', cv.WINDOW_NORMAL)
            cv.imshow('win_name', frame)

            out.write(frame)  # 将每一帧写入文件

        if cv.waitKey(25) == 27:  # 按键盘上的 q 或 esc 退出（在英文输入法下）
            break
    cap.release()  # 释放读的资源
    out.release()  # 释放写的资源
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
