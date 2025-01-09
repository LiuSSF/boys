import subprocess
from Xlib import display

# 获取 Google Chrome 窗口的几何信息
def get_chrome_window_geometry():
    d = display.Display()
    root = d.screen().root
    window_ids = root.get_full_property(d.intern_atom('_NET_CLIENT_LIST'), display.X.AnyPropertyType).value

    for window_id in window_ids:
        window = d.create_resource_object('window', window_id)
        window_name = window.get_full_property(d.intern_atom('_NET_WM_NAME'), 0).value.decode('utf-8')

        # 找到 Google Chrome 窗口
        if "Google Chrome" in window_name:
            geom = window.get_geometry()
            return geom.x, geom.y, geom.width, geom.height

    return None

# 使用 scrot 截取指定区域的截图
def capture_chrome_window(x, y, width, height,filename):
    # 指定您要截取的区域
    print(f"Capturing region: {x}, {y}, {width}x{height}")

    # 使用 scrot 截取窗口截图
    subprocess.run(["scrot", "-a", f"{x},{y},{width},{height}", filename])
    print(f"Screenshot saved as {filename}")
    


# 调用截图函数

