
## 0707更新
### 终端检查工具工具-指定盘符版 V1.1

（部分windows7电脑需要打KB2533623补丁，请自行到官网下载）

> 更新情况

> （1）增加了线程控制功能，用户可以通过界面上输入扫描速度，切换不同的线程。数字越小，扫描速度越慢，终端损耗的资源越小

> （2）增加了实时扫描记录功能，扫描发现的问题会实时记录到scan_all_results.txt

![11](https://github.com/bingtangbanli/Data-security-check/assets/77956516/4079a292-af7e-4a69-b70c-0c7e95c0ebf9)

## 其他工具介绍

### 一、windows各类型文件梳理

使用方法：双击bat文件即可查看windows电脑上所有的excel、exe和zip文件。
这些文件的结果分别保存在同级目录下的excel_files.txt、exe_files.txt和zip_files.txt和txts.txt和Words.txt

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/7debe6d3-95f4-42f4-9da0-f823e9539de9)

扫描结果：

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/b5755a9d-1718-4770-b2e3-a0523a98e16d)

txt文件中具体结果显示了文件+具体的路径

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/b27fcf59-b2d8-4469-afce-3ce9ead67ecd)

### 二、windows电脑查看IP地址

主要是帮助非IT人员，查看自己的电脑IP地址

使用方法：双击即可
![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/dcbf81f6-ef3c-4f9e-9379-9aeef9708e52)


### 三、windows电脑 远程软件安装检查

主要是检查电脑上是否有Todesk、TeamViewer、蒲公英、向日葵软件

原理是根据注册表的信息进行查询，因此如果历史安装过这些软件，但是没有卸载干净，也会被检测出来

使用方法：选择bat文件或者exe文件，双击即可

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/27202005-e154-4049-84e2-10b89f0aa4b0)

### 四、终端检查工具-指定文件夹版

（部分windows7电脑需要打KB2533623补丁，请自行到官网下载）

主要检查电脑指定文件夹下的word文件、txt文件、excel文件是否含有手机号或者身份证号

检查结果，工具上有显示 和 有问题的文件会保存到本地的scan_results.tx文件中

使用方法：双击Check_Tool2_GUI文件，点击Browse 选择文件夹即可，之后开始扫描（正在被占用的文件不会被扫描到）

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/26a092be-4d4f-419b-aa97-bd01eaa68c69)

扫描结果

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/6d166155-ad52-472e-abae-eb518dcea309)
![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/edede692-d9f7-467b-a510-cc02df94c9ce)
![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/efe8f225-453f-4579-aacf-9510e220a343)
![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/5a151d8f-b1ea-412d-b896-b857b5dc356c)

### 五、终端检查工具工具-指定盘符版

（部分windows7电脑需要打KB2533623补丁，请自行到官网下载）

主要检查电脑指定盘符下的word文件、txt文件、excel文件是否含有手机号或者身份证号。（盘符可以多选扫描，按住shift多选）

检查结果，工具上有显示 和 有问题的文件会保存到本地的文件中

使用方法：双击Check_Tool_GUI.exe文件，选择盘符开始扫描（正在被占用的文件不会被扫描到）

备注：该工具启动会检测电脑上有哪些盘符，所以启动会较慢。另外点击开始扫描。工具会先匹配指定盘符下的word、txt、excel文件，再开始扫描。因此速度较慢。请耐心等待2~5分钟。

使用截图如下：

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/d456ff84-8e20-4663-be8a-d3df626daac0)
![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/6dceda61-e51a-42e7-9474-aa6d2c8503d0)
![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/0e4e59ac-fd0a-430a-b56b-dab57b252f8e)

### 六、文件批量复制

（部分windows7电脑需要打KB2533623补丁，请自行到官网下载）

该工具主要是配合第一个工具的。第一个工具扫描的结果 所保存的txt文件。此工具可以将该文件全部打包复制到result文件夹下

使用方法：双击运行exe软件（选择的路径，文件夹名之间不能有空格）
注意事项：该工具执行了批量复制的操作，可能被杀毒软件误报

使用举例
复制之前第一个文件查出来的所有的excel文件
选择excel_files.txt

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/fe0de9ad-f34a-47ac-b4ab-3111942659b1)


点击开始复制，则txt中excel文件均被复制到cp_file.exe的同级目录result文件夹下

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/c0361dd5-bda1-4b82-aca0-344fdb0641c0)

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/3005e1ec-a6b6-45d0-a697-ec37730f0485)


### 七、一键删除工具

（部分windows7电脑需要打KB2533623补丁，请自行到官网下载）

本工具主要配合终端检查工具使用，方便一键删除
使用方法：双击exe文件启动，选择合终端检查工具检测扫描结果的txt文件。 可以一键删除txt文件中包含的excel、word、txt文件

注意事项：
（1）删除后 文件无法恢复
（2）工具涉及批量删除，可能被杀毒软件误报

使用截图

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/fa0ab528-14d4-4ca8-9b52-84305ac32013)

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/d3dc73f8-ea86-41ff-8d51-93d7244df97e)

![image](https://github.com/bingtangbanli/Data-security-check/assets/77956516/158b8ed7-6a2a-4960-9887-e11ee6966cb0)


