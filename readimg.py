import cv2
import os

def readimg(img):
    # 加载模板库
    template_folder = "card_templates"
    templates = {}

    # 遍历模板文件夹，加载每张牌的模板
    for file_name in os.listdir(template_folder):
        if file_name.endswith(".png"):
            # 读取模板图像并转换为灰度
            template = cv2.imread(os.path.join(template_folder, file_name), cv2.IMREAD_GRAYSCALE)
            if template is None:
                print(f"Error: Unable to load template image {file_name}. Skipping this template.")
                continue
            # 应用高斯模糊
            template = cv2.GaussianBlur(template, (5, 5), 0)

            # 去除文件扩展名，得到牌面名称，例如：clubs_A
            card_name = os.path.splitext(file_name)[0]
            # 存入字典，键为牌面名称，值为模板图像
            templates[card_name] = template

    # 定义待识别的图像路径
    input_image_path = img
    input_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if input_image is None:
        print("Error: Unable to load input image. Please check the file path.")
        exit()

    # 对输入图像应用高斯模糊
    input_image = cv2.GaussianBlur(input_image, (5, 5), 0)

    # 调整输入图像的尺寸
    input_image_resized = cv2.resize(input_image, (77, 96))  # 假设模板大小为 77x96

    # 初始化匹配结果
    best_match_name = None
    best_match_score = 0

    # 遍历模板库进行匹配
    for card_name, template in templates.items():
        # 调整模板图像大小，以匹配输入图像
        template_resized = cv2.resize(template, (input_image_resized.shape[1], input_image_resized.shape[0]))

        # 使用模板匹配算法，得到匹配结果
        result = cv2.matchTemplate(input_image_resized, template_resized, cv2.TM_CCOEFF_NORMED)
        
        # 获取匹配结果的最大值，作为匹配分数
        _, max_val, _, _ = cv2.minMaxLoc(result)
        #print(f"Matching score for {card_name}: {max_val}")  # 输出每个模板的匹配得分（调试信息）

        # 更新最佳匹配
        if max_val > best_match_score:
            best_match_score = max_val
            best_match_name = card_name

    # 设置匹配阈值，例如0.4以上为匹配成功
    threshold = 0.5
    if best_match_score >= threshold:
        print(f"匹配成功：识别的牌面为 {best_match_name}，匹配得分为 {best_match_score}")
        return best_match_name.split('-')[0] # 返回牌面 - 左边
    else:
        print("未能匹配到任何模板牌面，可能不是有效的扑克牌。")
        return 0
#print(readimg("1.png"))