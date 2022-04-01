import cv2 as cv

# video = 'video/video_out.avi'
video = 'video/video_deal_out.avi'


def main():
    cap = cv.VideoCapture(video)  # 读取视频
    retval_width = cap.get(3)  # 获取视频的宽高
    retval_height = cap.get(4)  # 获取视频的宽高
    retval_fps = cap.get(5)  # 获取视频的FPS
    print('Video_width:{:.0f}\nVideo_height:{:.0f}\nVideo_FPS:{:.0f}\n'
          .format(retval_width, retval_height, retval_fps))

    while cap.isOpened():
        # display
        ret, frame = cap.read()
        print(ret)
        if ret:
            # cv.putText(frame, 'Video_FPS {0}'.format(retval_fps), (0, 50),
            #            cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 5)
            cv.namedWindow('win_name', cv.WINDOW_NORMAL)
            cv.imshow('win_name', frame)

        if cv.waitKey(25) == 27:  # 按键盘上的 q 或 esc 退出（在英文输入法下）
            break
    cap.release()  # 释放读的资源
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
