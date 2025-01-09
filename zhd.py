from PIL import Image
import os

# 指定目录路径
directory = "card_templates"

# 遍历目录下所有文件
for filename in os.listdir(directory):
    if filename.endswith(".png"):  # 只处理 PNG 文件
        file_path = os.path.join(directory, filename)
        
        # 打开图片
        img = Image.open(file_path)
        
        # 转换为灰度图像
        grayscale_img = img.convert("L")
        
        # 保存灰度图像，覆盖原文件或保存为其他路径
        grayscale_img.save(file_path)
        print(f"{filename} 已转换为灰度")
