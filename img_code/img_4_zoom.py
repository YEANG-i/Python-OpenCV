import cv2 as cv

img_input = 'img/xl_4.jpg'


def main():
    img = cv.imread(img_input, 1)

    print(img.shape, img.size)
    img_zoom_1 = cv.resize(img, None, fx=0.5, fy=0.5)
    print(img_zoom_1.shape, img_zoom_1.size)
    img_zoom_2 = cv.resize(img, None, fx=1.5, fy=1.5)
    print(img_zoom_2.shape, img_zoom_2.size)

    cv.imshow("name_0", img)
    cv.imshow('name_1', img_zoom_1)
    cv.imshow('name_2', img_zoom_2)

    cv.waitKey(0)


if __name__ == "__main__":
    main()
