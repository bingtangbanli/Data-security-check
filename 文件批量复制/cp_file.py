import os
import shutil
import chardet

# 获取用户输入的txt文件路径，以空格分隔多个文件
txt_files_input = input("请输入包含文件路径的txt文件路径，多个文件请用空格分隔: ")
txt_files = txt_files_input.split()

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
        absolute_paths = file.read().splitlines()

    # 复制每个绝对路径指定的文件到result文件夹
    for path in absolute_paths:
        if os.path.exists(path):
            try:
                file_name = os.path.basename(path)
                destination_path = os.path.join(result_folder, file_name)

                if os.path.exists(destination_path):
                    # 生成新的文件名
                    base_name, extension = os.path.splitext(file_name)
                    counter = 1
                    while True:
                        new_file_name = f"{base_name}_{counter}{extension}"
                        new_destination_path = os.path.join(result_folder, new_file_name)
                        if not os.path.exists(new_destination_path):
                            destination_path = new_destination_path
                            break
                        counter += 1

                shutil.copy2(path, destination_path)
                print(f"已复制文件: {file_name}")
            except PermissionError:
                print(f"文件被其他进程占用，跳过复制: {path}")
        else:
            print(f"文件不存在: {path}")

print("所有文件复制完成")
