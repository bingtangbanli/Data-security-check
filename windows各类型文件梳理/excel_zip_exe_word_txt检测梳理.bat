@echo off
chcp 936 > nul
setlocal enabledelayedexpansion

set OutputFileExe=exe_files.txt
set OutputFileExcel=excel_files.txt
set OutputFileZip=zip_files.txt
set OutputFileTxt=txts.txt
set OutputFileWords=Words.txt

echo ���ڲ�ѯ.exe�ļ�...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo ���ڲ�ѯ�̷� %%D...
    dir /s /b "%%D:\*.exe" >> %OutputFileExe%
)
echo ��ѯ���
echo ����ѱ��浽 %OutputFileExe%

echo ���ڲ�ѯExcel�ļ�...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo ���ڲ�ѯ�̷� %%D...
    dir /s /b "%%D:\*.xlsx" "%%D:\*.xls" >> %OutputFileExcel%
)
echo ��ѯ��ɣ�
echo ����ѱ��浽 %OutputFileExcel%

echo ���ڲ�ѯ.zip�ļ�...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo ���ڲ�ѯ�̷� %%D...
    dir /s /b "%%D:\*.zip" >> %OutputFileZip%
)
echo ��ѯ���
echo ����ѱ��浽 %OutputFileZip%

echo ���ڲ�ѯ.txt�ļ�...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo ���ڲ�ѯ�̷� %%D...
    dir /s /b "%%D:\*.txt" >> %OutputFileTxt%
)
echo ��ѯ���
echo ����ѱ��浽 %OutputFileTxt%

echo ���ڲ�ѯWord�ļ�...
for %%D in (C D E F G H I J K L M N O P Q R S T U V W X Y) do (
    echo ���ڲ�ѯ�̷� %%D...
    dir /s /b "%%D:\*.docx" "%%D:\*.doc" >> %OutputFileWords%
)
echo ��ѯ��ɣ�
echo ����ѱ��浽 %OutputFileWords%

echo �밴������رգ�
pause > nul
