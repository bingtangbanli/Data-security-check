@echo off
chcp 936 > nul

title 显示您的IP
ipconfig
echo ------------------------------------------------------
for /f "tokens=2 delims=:" %%i in ('ipconfig ^| findstr "IPv4"') do set ip=%%i
echo ======================== Your IP Address is: %ip% ========================
echo ------------------------------------------------------
echo.

pause > nul

