import cv2 as cv
import numpy as np

img_input_1 = 'img/xl_1.jpg'


def main():
    img_1 = cv.imread(img_input_1)

    # deal
    kernel = np.ones((10, 10), np.uint8)
    # 开运算 闭运算
    cv_open = cv.morphologyEx(img_1, cv.MORPH_OPEN, kernel)  # 开运算
    cv_close = cv.morphologyEx(img_1, cv.MORPH_CLOSE, kernel)  # 闭运算
    # 礼帽 黑帽
    cv_top_hat = cv.morphologyEx(img_1, cv.MORPH_TOPHAT, kernel)  # 礼帽
    cv_black_hat = cv.morphologyEx(img_1, cv.MORPH_BLACKHAT, kernel)  # 黑帽

    # cv.namedWindow('win_name', cv.WINDOW_NORMAL)
    cv.imshow('0', img_1)
    cv.imshow('1', cv_open)
    cv.imshow('2', cv_close)
    cv.imshow('3', cv_top_hat)
    cv.imshow('4', cv_black_hat)
    cv.waitKey(0)

    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
