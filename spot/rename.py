import os

folder_path = os.path.join(os.path.dirname(__file__), "images")
files = os.listdir(folder_path)

files.sort() # 按原始名字排列
# 为每个文件创建新的文件名并重命名
for i, filename in enumerate(files):
    _, ext = os.path.splitext(filename)  # 获取文件扩展名
    new_filename = f"image_{i + 1}{ext}"  # 创建新文件名
    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

print("文件重命名完成！")
