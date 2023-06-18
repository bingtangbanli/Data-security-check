@echo off
chcp 65001 > nul

echo 正在检查是否安装ToDesk...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\ToDesk" >nul 2>&1
if %errorlevel%==0 (
echo [已安装ToDesk]
) else (
echo [未安装ToDesk]
)
echo.

echo 正在检查是否安装向日葵...
reg query "HKEY_CURRENT_USER\SOFTWARE\Oray" >nul 2>&1
if %errorlevel%==0 (
echo [已安装向日葵]
) else (
echo [未安装向日葵]
)
echo.

echo 正在检查是否安装TeamViewer...
reg query "HKEY_CLASSES_ROOT\TeamViewerSession" >nul 2>&1
if %errorlevel%==0 (
echo [已安装TeamViewer]
) else (
echo [未安装TeamViewer]
)
echo.

echo 正在检查是否安装蒲公英...
reg query "HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\PgyVisitor" >nul 2>&1
if %errorlevel%==0 (
echo [已安装蒲公英]
) else (
echo [未安装蒲公英]
)
echo.

echo 请按任意键关闭！
pause >nul