import cv2

img_input = 'img/xl_5.jpg'


def main():
    img = cv2.imread(img_input, 1)  # 1、0、-1分别对应图像的彩色、灰度、alpha通道的加载图像模式。默认1

    # save img
    cv2.imwrite('img_save_name.png', img)
    img_save = cv2.imread('img_save_name.png', 1)  # 读取灰度图，无法改变参数
    cv2.imshow('img_save_window_name', img_save)

    cv2.namedWindow('window_name', cv2.WINDOW_NORMAL)
    cv2.imshow('window_name', img)
    # cv2.waitKey(1) in ['24', '28']:
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
