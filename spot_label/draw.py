import cv2
import numpy as np
import os

# 绘制直线轨道（直走情况中）
def draw_track_straight(image, track_width, width, height):
    left_line_x = np.random.randint(0.25*width, 0.75*width)
    right_line_x = left_line_x+track_width
    left_start_point = (left_line_x, height)
    left_end_point = (left_line_x, 0)
    right_start_point = (right_line_x, height)
    right_end_point = (right_line_x, 0)
    line_color = (0, 0, 0)  # BGR 颜色
    line_thickness = 2
    cv2.line(image, left_start_point, left_end_point, line_color, line_thickness)
    cv2.line(image, right_start_point, right_end_point, line_color, line_thickness)

# 绘制起始直线轨道（转弯情况中）
def draw_track_before_turn(image, track_width, width, height):
    left_line_x = np.random.randint(0.25*width, 0.75*width)
    line_len = np.random.randint(0.25*height, 0.75*height)

    left_start_point = (left_line_x, height-1)
    global left_end_point
    left_end_point = (left_line_x, height-line_len-1)

    right_line_x = left_line_x + track_width
    right_start_point = (right_line_x, height-1)
    global right_end_point
    right_end_point = (right_line_x, height-line_len-1)

    global line_color  
    global line_thickness
    line_color = (0, 0, 0)  # BGR 颜色
    line_thickness = 2
    cv2.line(image, left_start_point, left_end_point, line_color, line_thickness)
    cv2.line(image, right_start_point, right_end_point, line_color, line_thickness)

# 绘制右转圆弧
def draw_turn_right_circle(image, track_width):
    global small_radius, large_radius
    small_radius = np.random.randint(2*track_width, 5*track_width)
    large_radius = small_radius +track_width
    center = (right_end_point[0]+small_radius,right_end_point[1])
    small_axes = (small_radius, small_radius)
    large_axes = (large_radius, large_radius)
    angle = 0
    start_angle = -180
    end_angle = -90
    cv2.ellipse(image, center, small_axes, angle, start_angle, end_angle, line_color, line_thickness)
    cv2.ellipse(image, center, large_axes, angle, start_angle, end_angle, line_color, line_thickness)

# 绘制左转圆弧
def draw_turn_left_circle(image, track_width):
    global small_radius, large_radius
    small_radius = np.random.randint(2*track_width, 5*track_width)
    large_radius = small_radius +track_width
    center = (left_end_point[0]-small_radius,left_end_point[1])
    small_axes = (small_radius, small_radius)
    large_axes = (large_radius, large_radius)
    angle = 0
    start_angle = 0
    end_angle = -90
    cv2.ellipse(image, center, small_axes, angle, start_angle, end_angle, line_color, line_thickness)
    cv2.ellipse(image, center, large_axes, angle, start_angle, end_angle, line_color, line_thickness)

# 绘制右转终止直线
def draw_turn_after_right_circle(image, track_width, width):
    below_start_point = (right_end_point[0]+small_radius, right_end_point[1]-small_radius)
    upper_start_point = (below_start_point[0], below_start_point[1]-track_width)
    below_end_point = (width, below_start_point[1])
    upper_end_point = (width, upper_start_point[1])
    cv2.line(image, below_start_point, below_end_point, line_color, line_thickness)
    cv2.line(image, upper_start_point, upper_end_point, line_color, line_thickness)

# 绘制左转终止直线
def draw_turn_after_left_circle(image, track_width):
    below_start_point = (left_end_point[0]-small_radius, left_end_point[1]-small_radius)
    upper_start_point = (below_start_point[0], below_start_point[1]-track_width)
    below_end_point = (0, below_start_point[1])
    upper_end_point = (0, upper_start_point[1])
    cv2.line(image, below_start_point, below_end_point, line_color, line_thickness)
    cv2.line(image, upper_start_point, upper_end_point, line_color, line_thickness)

output_dir = os.path.join(os.path.dirname(__file__), 'images')
height = 480
width = 640


# 开始绘制
for i in range(100):
    image = np.full((height, width, 3), 255, dtype=np.uint8)  # 每次循环都创建一个新的图像
    track_width = np.random.randint(30,70)
    image_status = np.random.randint(0,3)
    if image_status == 0:
        # 直走
        draw_track_straight(image, track_width, width, height)
    elif image_status == 1:
        # 右转
        draw_track_before_turn(image, track_width, width, height)
        draw_turn_right_circle(image,track_width)
        draw_turn_after_right_circle(image, track_width, width)
        
    elif image_status == 2:
        # 左转
        draw_track_before_turn(image, track_width, width, height)
        draw_turn_left_circle(image,track_width)
        draw_turn_after_left_circle(image, track_width)
    
    # 保存图像
    filename = os.path.join(output_dir, f"image_{i+1}.jpg")
    cv2.imwrite(filename, image)
    print(str(i) + ":" + str(track_width))