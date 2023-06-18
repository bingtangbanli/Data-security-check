import os
import PySimpleGUI as sg

def delete_files(file_paths):
    deleted_files = []
    not_found_files = []

    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            deleted_files.append(file_path)
        else:
            not_found_files.append(file_path)

    sg.popup("删除完成。")
    if deleted_files:
        deleted_files_str = '\n'.join(deleted_files)
        sg.popup_scrolled("已删除的文件:\n\n" + deleted_files_str, title='已删除的文件')
    if not_found_files:
        not_found_files_str = '\n'.join(not_found_files)
        sg.popup_scrolled("未找到的文件:\n\n" + not_found_files_str, title='未找到的文件')

sg.theme("DefaultNoMoreNagging")

layout = [
    [sg.Text("选择包含文件路径的文本文件：")],
    [sg.Input(key="-TXT_FILE-"), sg.FileBrowse()],
    [sg.Button("删除", key="-DELETE-")]
]

window = sg.Window("一键文件删除工具(by 冰糖葫芦)", layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break

    if event == "-DELETE-":
        txt_file = values["-TXT_FILE-"]
        if not os.path.exists(txt_file):
            sg.popup(f"文件 {txt_file} 不存在。")
            continue

        file_paths = []
        with open(txt_file, 'r') as file:
            for line in file:
                file_path = line.strip()
                if os.path.exists(file_path):
                    file_paths.append(file_path)
                else:
                    sg.popup(f"文件 {file_path} 不存在。")

        if sg.popup_yes_no("删除后的文件无法恢复，是否继续？") == "Yes":
            delete_files(file_paths)

window.close()
