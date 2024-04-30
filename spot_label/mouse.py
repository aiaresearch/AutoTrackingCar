import cv2
import os

def mousecallback(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print(x, y)

image_dir = "images"
image_files = sorted(os.listdir(image_dir))  # 确保图像按顺序加载
start_image = 0
current_image_index = start_image

while True:
    image_path = os.path.join(image_dir, image_files[current_image_index])
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to read image: {image_path}")
        break

    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mousecallback)

    key = cv2.waitKey(0)
    if key == ord('a') and current_image_index > 0:  # 上一张图片
        current_image_index -= 1
    elif key == ord('d') and current_image_index < len(image_files) - 1:  # 下一张图片
        current_image_index += 1
    elif key == 27:  # ESC键退出循环
        break

cv2.destroyAllWindows()
