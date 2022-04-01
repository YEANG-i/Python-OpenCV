import cv2 as cv

img_input_1 = 'img/xl_1.jpg'
img_input_2 = 'img/xl_2.jpg'


def main():
    img_1 = cv.imread(img_input_1, 1)
    img_2 = cv.imread(img_input_2, 1)
    print(img_1.shape, img_1.size)
    print(img_2.shape, img_2.size)

    # add加法
    # img_add = cv.add(img_1, img_2)
    # print(img_add.shape, img_add.size)
    # cv.namedWindow('win_name', img)
    # cv.imshow('1', img_1)
    # cv.imshow('2', img_2)
    # cv.imshow('add', img_add)

    # 混合
    img_add_weight = cv.addWeighted(img_1, 0.8, img_2, 0.2, 0)
    cv.imshow('add_weight', img_add_weight)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
