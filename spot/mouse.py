import cv2
import os
import re

# 定义绘制点击位置的函数
def draw_cross(image, x, y, color=(0, 0, 255), thickness=2, size=10):
    cv2.line(image, (x - size, y), (x + size, y), color, thickness)
    cv2.line(image, (x, y - size), (x, y + size), color, thickness)

def mousecallback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        # 在图像上绘制点击位置
        draw_cross(param[1], x, y)
        # 在点击位置显示坐标
        # cv2.putText(param[1], f"({x}, {y})", (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        # 获取当前图像文件名
        current_image_filename = param[0]
        # 创建文本文件名（与图像文件名相同，但扩展名改为.txt）
        label_file = os.path.join("labels", os.path.splitext(current_image_filename)[0] + ".txt")
        # 将鼠标点击位置坐标写入文本文件
        with open(label_file, 'a') as f:
            f.write(f"{x} {y}\n")  # 将坐标写入文件，并在每个坐标后添加换行符
        # 保存带有点击位置标记的图像到另一个文件夹
        # output_folder = param[2]
        # output_image_path = os.path.join(output_folder, current_image_filename)
        # cv2.imwrite(output_image_path, param[1])

# 设置输入和输出文件夹路径
# output_image_dir = "output_images"

# 确保输出文件夹存在
# os.makedirs(output_image_dir, exist_ok=True)
os.makedirs("labels", exist_ok=True)

# 获取输入图像文件列表，并按顺序加载
image_dir = "output_images"
image_files = sorted(os.listdir(image_dir), key=lambda x: int(re.findall(r'\d+', x)[0]))
start_image = 0
current_image_index = start_image

while True:
    # print(current_image_index)
    # print(image_files)
    if image_files == []:
        print("No images found")
        break
    image_filename = image_files[current_image_index]
    # print(image_filename)
    # print(image_files)
    image_path = os.path.join(image_dir, image_filename)
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to read image: {image_path}")
        break

    # 创建一个副本图像以在上面绘制点击位置，以避免覆盖源文件
    # display_image = image.copy()
    
    cv2.imshow("Image", image)
    cv2.setMouseCallback("Image", mousecallback, param=(image_filename, image, image_files))  # 将当前图像文件名和图像副本以及输出文件夹作为参数传递给回调函数
    key = cv2.waitKey(0)
    if key == ord('a') and current_image_index > 0:
        current_image_index -= 1
        print(image_filename)
        image_file_split = image_filename.split(".")
        current_label_dir = os.path.join("labels", image_file_split[0])+".txt"
        print(current_label_dir)
    elif key == ord('d') and current_image_index < len(image_files) - 1:
        current_image_index += 1
    elif key == 27:  # ESC键退出循环
        break

cv2.destroyAllWindows()
