import cv2


blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
img_input = 'img/xl_5.jpg'


def main():
    # img = np.zeros((512, 512, 3), np.uint8)
    img = cv2.imread(img_input, 1)  # 1、0、-1分别对应图像的彩色、灰度、alpha通道的加载图像模式。默认1

    # get the shape x, y = 750, 1200
    x, y, z = img.shape[0], img.shape[1], img.shape[2]
    print('shape: x:{},y:{},z:{}'.format(x, y, z))
    img_size = img.size
    print('size:{0}'.format(img_size))
    img_dtype = img.dtype
    print('dtype:{0}'.format(img_dtype))

    # Draw line
    cv2.line(img, (0, 20), (1200, 20), red, 5)
    cv2.circle(img, (300, 300), 63, red, 5)
    cv2.rectangle(img, (50, 50), (1150, 700), red, 5)
    cv2.putText(img, 'shape: x:{},y:{},z:{}'.format(x, y, z), (55, 150),
                cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 3, green, 5)

    # display the img
    cv2.namedWindow('window_name', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('window_name', img)
    # # cv2.waitKey(1) in ['24', '28']:
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
