import os
import shutil
import chardet
from openpyxl import load_workbook
import PySimpleGUI as sg

# GUI布局
layout = [
    [sg.Text("包含文件路径的txt文件路径："), sg.Input(key="-TXT_FILES-"), sg.FileBrowse()],
    [sg.Button("开始复制"), sg.Button("退出")]
]

def copy_files(txt_files):
    # 创建result文件夹（如果不存在）
    result_folder = "result"
    if not os.path.exists(result_folder):
        os.makedirs(result_folder)

    # 复制文件
    for txt_file in txt_files:
        # 检测文件编码
        with open(txt_file, "rb") as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result["encoding"]

        # 读取txt文件中的每个绝对路径
        with open(txt_file, "r", encoding=encoding) as file:
            lines = file.read().splitlines()

        # 复制每个绝对路径指定的文件到result文件夹
        for path in lines:
            if os.path.exists(path):
                try:
                    file_name = os.path.basename(path)
                    destination_path = os.path.join(result_folder, file_name)

                    # 复制文件，如果存在相同文件名则直接覆盖
                    shutil.copy(path, destination_path)
                    print(f"已复制文件: {file_name}")
                except PermissionError:
                    print(f"文件被其他进程占用，跳过复制: {path}")
            else:
                print(f"文件不存在: {path}")

    print("所有文件复制完成")
    sg.Popup("文件复制完成", f"文件保存在：{result_folder}文件夹下")

# 创建窗口
window = sg.Window("文件复制工具(by冰糖葫芦)", layout)

# 事件循环
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "退出":
        break
    elif event == "开始复制":
        txt_files_input = values["-TXT_FILES-"]
        if txt_files_input:
            txt_files = txt_files_input.split()
            copy_files(txt_files)

window.close()
