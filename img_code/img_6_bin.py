import cv2 as cv
from matplotlib import pyplot as plt

img_input_1 = 'img/xl_5.jpg'


def main():
    img = cv.imread(img_input_1)
    cv.imshow('0', img)

    histr_0 = cv.calcHist([img], [0], None, [256], [0, 256])
    histr_1 = cv.calcHist([img], [1], None, [256], [0, 256])
    histr_2 = cv.calcHist([img], [2], None, [256], [0, 256])
    plt.figure(figsize=(10, 6), dpi=100)
    plt.plot(histr_0)
    plt.plot(histr_1)
    plt.plot(histr_2)
    plt.grid()
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
