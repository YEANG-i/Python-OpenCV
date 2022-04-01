import cv2 as cv
from matplotlib import pyplot as plt

# 1 读取图像
img = cv.imread('img/xl_1.jpg', 0)
# 2 计算Sobel卷积结果
# x = cv.Sobel(img, cv.CV_16S, 1, 0)
# y = cv.Sobel(img, cv.CV_16S, 0, 1)
# 将上述代码中计算sobel算子的部分中将ksize设为-1，就是利用Scharr进行边缘检测。
x = cv.Sobel(img, cv.CV_16S, 1, 0, ksize=-1)
y = cv.Sobel(img, cv.CV_16S, 0, 1, ksize=-1)
# 3 将数据进行转换
Scale_absX = cv.convertScaleAbs(x)  # convert 转换  scale 缩放
Scale_absY = cv.convertScaleAbs(y)
# 4 结果合成
result = cv.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
# 5 图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.subplot(121), plt.imshow(img, cmap=plt.cm.gray), plt.title('xl_1.jpg')
plt.xticks([]), plt.yticks([])

plt.subplot(122), plt.imshow(result, cmap=plt.cm.gray), plt.title('Sobel——xl_1.jpg')
plt.xticks([]), plt.yticks([])
plt.show()
