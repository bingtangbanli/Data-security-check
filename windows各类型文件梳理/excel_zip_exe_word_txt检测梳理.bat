@echo off
chcp 936 > nul
setlocal enabledelayedexpansion

set OutputFileExe=exe_files.txt
set OutputFileExcel=excel_files.txt
set OutputFileZip=zip_files.txt
set OutputFileTxt=txts.txt
set OutputFileWords=Words.txt

echo 正在查询.exe文件...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo 正在查询盘符 %%D...
    dir /s /b "%%D:\*.exe" >> %OutputFileExe%
)
echo 查询完成
echo 结果已保存到 %OutputFileExe%

echo 正在查询Excel文件...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo 正在查询盘符 %%D...
    dir /s /b "%%D:\*.xlsx" "%%D:\*.xls" >> %OutputFileExcel%
)
echo 查询完成！
echo 结果已保存到 %OutputFileExcel%

echo 正在查询.zip文件...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo 正在查询盘符 %%D...
    dir /s /b "%%D:\*.zip" >> %OutputFileZip%
)
echo 查询完成
echo 结果已保存到 %OutputFileZip%

echo 正在查询.txt文件...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo 正在查询盘符 %%D...
    dir /s /b "%%D:\*.txt" >> %OutputFileTxt%
)
echo 查询完成
echo 结果已保存到 %OutputFileTxt%

echo 正在查询Word文件...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo 正在查询盘符 %%D...
    dir /s /b "%%D:\*.docx" "%%D:\*.doc" >> %OutputFileWords%
)
echo 查询完成！
echo 结果已保存到 %OutputFileWords%

echo 请按任意键关闭！
pause > nul
