import base64
import screenshot
import glob
import os
import time
import readimg
from datetime import datetime
from flask import Flask, request, jsonify
from flask_cors import CORS
import pairs
app = Flask(__name__)
CORS(app)  # 允许所有来源的跨域请求
os.environ["DISPLAY"] = ":0" 
# openai()
#result = readimg.readimg("1.png")
#print(result)
def readnum():
    try:
        screenshot.capture_chrome_window(548, 517+18, 20, 23, '1.png')
        time.sleep(0.5)
        screenshot.capture_chrome_window(548 + 26, 515+18, 20, 23, '2.png')
        time.sleep(0.5)
        result = readimg.readimg('1.png')
        result1 = readimg.readimg('2.png')
        # 检查1.png是否存在，存在则删除
        if os.path.exists('1.png'):
            os.remove('1.png')
        
        # 检查2.png是否存在，存在则删除
        if os.path.exists('2.png'):
            os.remove('2.png')
        return result+result1
    except:
        return '00'

@app.route('/receive', methods=['POST'])
def receive_info():
    # 获取 JSON 数据
    data = request.get_json()
    print(data)
    # 检查数据是否有效
    if data:
        # 获取当前时间
        now = datetime.now()
        # 提取数据内容，例如获取 "message" 键的值
        message = data.get('message', 'No message provided')
        num = readnum() # 识别牌面
        print("num===========:",num,"----",now)
        ok = pairs.is_in_top_pairs(num) #检查是否在牌型中 有则返回True
        # 创建响应数据
        print("ok=======",ok,"----",now)
        #ok = True
        response = {
            'received': ok,
            'status': 'success',
            'message': f"Received: {message}"
        }
        time.sleep(0.5)
    else:
        # 错误处理
        response = {
            'status': 'error',
            'message': 'No JSON data received'
        }
    # 返回 JSON 响应
    return jsonify(response)
if __name__ == '__main__':
    #查找并删除当前文件夹下的所有 PNG 文件
    for file_path in glob.glob('*.png'):
        os.remove(file_path)
        print(f"已删除: {file_path}")
    app.run(debug=True)
    # screenshot.capture_chrome_window(548, 517, 20, 23, '1.png')
    # time.sleep(0.5)
    # screenshot.capture_chrome_window(548 + 26, 515, 20, 23, '2.png')
    # time.sleep(0.5)
