import subprocess

def check_installed_software(reg_path):
    command = f'reg query "{reg_path}" > nul 2>&1'
    result = subprocess.call(command, shell=True)
    return result == 0

# 检查是否安装ToDesk
if check_installed_software('HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\ToDesk'):
    print('已安装ToDesk')
else:
    print('未安装ToDesk')

# 检查是否安装向日葵
if check_installed_software('HKEY_CURRENT_USER\\SOFTWARE\\Oray'):
    print('已安装向日葵')
else:
    print('未安装向日葵')

# 检查是否安装TeamViewer
if check_installed_software('HKEY_CLASSES_ROOT\\TeamViewerSession'):
    print('已安装TeamViewer')
else:
    print('未安装TeamViewer')

# 检查是否安装蒲公英
if check_installed_software('HKEY_LOCAL_MACHINE\\SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\PgyVisitor'):
    print('已安装蒲公英')
else:
    print('未安装蒲公英')

input('请按任意键关闭！')
