import cv2
import numpy as np
import random

# # 创建一个空白图像
# image = np.zeros((300, 400, 3), dtype=np.uint8)

# # 绘制直线
# start_point = (50, 50)
# end_point = (350, 250)
# color = (0, 0, 0)  # BGR 颜色
# thickness = 2
# cv2.line(image, start_point, end_point, color, thickness)

# # 绘制圆弧
# center = (200, 150)
# axes = (100, 50)
# angle = 0
# start_angle = 0
# end_angle = 180
# color = (0, 0, 255)  # BGR 颜色
# thickness = 2
# cv2.ellipse(image, center, axes, angle, start_angle, end_angle, color, thickness)

height = 480
width = 640
image = np.full((height, width, 3), 255, dtype=np.uint8)
# image = np.zeros((height, width, 3), dtype=np.uint8)
# image[:, :] = (255,255,255)

# 绘制直线
left_line_x = random.randint(0.25*width, 0.75*width)
left_line_len = random.randint(0.05*height, 0.75*height)
start_point = (height, left_line_x, height-1)
end_point = (random.randint(0, 0.75*height)
color = (0, 0, 0)  # BGR 颜色
thickness = 2
cv2.line(image, start_point, end_point, color, thickness)
# 显示图像
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
