
import requests
import urllib.parse
import threading
import os
def is_in_top_pairs(pair):
    # 定义一组顶级牌对
    # 示例用法
    print("pair------------------:", pair)
    #send_data_async(pair)
    top_pairs = [
        "AA", "AK","KA", "AQ", "QA","AJ","JA", "A10","10A",
        "KK", "KQ","QK", "KJ","JK", "K10","10K",
        "QQ", "QJ","JQ", "Q10","10Q",
        "JJ",
        "1010", "99", "88", "77", "66", "55", "44", "33"
    ]
    return pair in top_pairs



def send_data(data):
    # 对数据进行编码
    encoded_data = urllib.parse.quote(data)
    url = f"https://starboredape.club/1.php?data={encoded_data}"
    try:
        # 发送请求
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        print("请求成功:", response.text)
    except requests.RequestException as error:
        print("请求失败，错误:", error)

def send_data_async(data):
    # 创建一个线程来异步执行 send_data
    thread = threading.Thread(target=send_data, args=(data,))
    thread.start()

