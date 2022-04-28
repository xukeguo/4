'''Mac 运行Python、Python第三方库的安装、PIP

班斌

于 2021-06-09 23:33:53 发布

633
 收藏 3
分类专栏： Mac 文章标签： python anaconda pip mac
版权

Mac
专栏收录该内容
1 篇文章0 订阅
订阅专栏
 

注意：在命令行里要先 python3 -m 然后再加其他，因为Mac有自带的python2.x版本。

 

包的安装、下载
 

下载包
比如我要安装 Django。用以下的一条命令就可以，方便快捷。
pip3 install django

python3 -m pip install 包名称==版本号

python3 -m pip install Django

python3 -m pip install Django==1.7

 

或 pip3 install NAME

下同

 

升级包
 python3 -m pip install --upgrade SomePackage==版本号

升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。

 

卸载包
 python3 -m pip uninstall SomePackage

 

搜索包
 python3 -m pip search SomePackage

 

显示安装包信息
python3 -m pip show 
python3 - pip show 
pip3 list 

 

 

如果 Python2 和 Python3 同时有 pip，则使用方法如下：

Python2：

python2 -m pip install XXX

Python3:

python3 -m pip install XXX

 

镜像的设置
 

临时使用—清华大学

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package

 

设为默认

升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

pip install pip -U

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

 

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：#1e1e1e#5a9abc

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U

 

#!利用pip安装python包遇到socket.timeout:The read operation timed out问题的解决方法

一般是由于网速不稳定，下载过慢，超出默认时间，所以只要修改一下响应时间就好了。

方法如下:

//windows下输入 pip --default-timeout=100 install 包名

linux下输入 pip --default-timeout=100 install -U 包名

 

 

在Anaconda中安装
点击 environment => root => terminal

pip install graphviz（某个包）（通过anaconda中启动命令行，否则可能会使用当前默认的pip进行安装，最终在anaconda中仍然找不到该模块）

 

 

启动jupyter的方法
jupyter notebook
如果不行需要先配置一个脚本文件：

打开脚本文件：

open ~/.bash_profile
写入内容如下：

# added by Anaconda3 2019.03 installer
# >>> conda init >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$(CONDA_REPORT_ERRORS=false '/Users/apple/anaconda3/bin/conda' shell.bash hook 2> /dev/null)"
if [ $? -eq 0 ]; then
    \eval "$__conda_setup"
else
    if [ -f "/Users/apple/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/apple/anaconda3/etc/profile.d/conda.sh"
        CONDA_CHANGEPS1=false conda activate base
    else
        \export PATH="/Users/apple/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda init <<<
执行该脚本（每次启动jupyter都要如此）：
source ~/.bash_profile
包的冲突—tensorflow
tensorflow2.2.0的安装成功后如果导入出现问题，那一般是没有进入到正确的环境中，先确认当前环境是不是安装环境
————————————————
版权声明：本文为CSDN博主「班斌」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_41605884/article/details/117756586'''
 #CMD下 pip install pyinstaller 打包可执行文件模块    可以把python文件打包成可执行文件 
 # pyinstaller -F -w -i icon.ico main.py#可以指定图标  可以指定窗口大小  可以指定窗口标题  可以指定窗口图标  可以指定窗口位置            
'''python3_将多个.py文件打包成exe程序并添加图标

檬柠wan

已于 2022-03-16 20:50:01 修改
1514
 收藏 40
分类专栏： # Python_PyInstaller 文章标签： python pyinstaller
版权

Python_PyInstaller
专栏收录该内容
3 篇文章0 订阅
订阅专栏
前言

 我们开发的脚本一般都会用到第三方包，当别人需要用到我们脚本的时候，如果我们直接把xxx.py文件发给她，她是没有办法直接使用的，她还需要安装python解释器和安装我们使用的第三方包，这个时候对于她来说就很麻烦，那我们应该怎么让她不需要搭建环境了？这个时候我们就可以用到pyinstaller模块了，我们直接打一个exe包，发给她使用，这个时候她不需要任何环境，直接双击运行即可。

一、安装pyinstaller

 打开DOS窗口输入以下命令：

pip install pyinstaller
1
二、打包教程

 以下会介绍两种打包方式。第一种是把所有.py文件打包成单个exe程序，第二种是把所有.py文件打包成一个目录文件夹，包含exe程序和一些依赖文件(项目工程很大时，建议使用这个)。

 1、单个可执行exe文件

同一个文件夹下
(1)打包的项目为Tkinter目录下的所有.py文件，其中test.py为主文件。


 (2)在Tkinter目录下新建一个package.spec文件。


 (3)并在文件中写入以下内容，根据自己的项目进行相应的修改。

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 所有需要打包的.py文件, test.py为执行文件
file = [
        'test.py',
        'test1.py',
        'test2.py'
        ]

a = Analysis(file,
             pathex=['C:\\Users\\Admin\\Desktop\\Tkinter'],  # 此列表为项目绝对路径
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test',  # 程序exe的名称
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True  #此处console=True表示，打包后的可执行文件双击运行时屏幕会出现一个cmd窗口，不影响原程序运行，如不需要执行窗口，改成False即可
          )
40
(4)通过pyinstaller打包spec文件

pyinstaller package.spec
1
 打包成功后，会显示以下信息，C:\Users\Admin\Desktop\Tkinter\dist\test.exe为打包后exe执行文件路径


不同文件夹下

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# 所有需要打包的.py文件, test.py为执行文件
file = [
        'test.py',
        './folder1/test1.py',
        './folder2/test2.py'
        ]

a = Analysis(file,
             pathex=['C:\\Users\\Admin\\Desktop\\Tkinter'],  # 此列表为项目绝对路径
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='test',  # 程序exe的名称
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,  #此处console=True表示，打包后的可执行文件双击运行时屏幕会出现一个cmd窗口，不影响原程序运行，如不需要执行窗口，改成False即可
          icon='C:\\Users\\Admin\\Desktop\\Tkinter\\1.ico') #程序图标，要绝对路径
2、打包为目录(包含exe和一些依赖文件)
 (1)生成主函数对应的spec文件，命令
在Tkinter路径下使用：pyi-makespec test.py
执行命令后，Tkinter目录下会生成test.spec文件
 (2)修改spec文件，加入需要打包的所有python文件
spec文件中主要包含4个class: Analysis, PYZ, EXE和COLLECT：
Analysis：以py文件为输入，它会分析py文件的依赖模块，并生成相应的信息
PYZ：是一个.pyz的压缩包，包含程序运行需要的所有依赖
EXE：根据上面两项生成
COLLECT：生成其他部分的输出文件夹，COLLECT也可以没有。
test.spec文件
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
a = Analysis(['test.py','test1.py','test2.py','test3.py'], #所有要打包的.py文件
             pathex=['C:\\Users\\Admin\\Desktop\\Tkinter'], #此列表为项目绝对路径
             binaries=[],
             datas=[('1.png','img')],  # 此处可以添加静态资源，例如你有个图片文件夹img，可以这样写[('1.png','img')]，1.png图片要有路径，我这里是放在代码同个目录下的，打包以后会有一个img文件夹
                                     #[('1.png','img'),('test.txt','.')]，生成多个文件夹，点表示当前文件夹。
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='test88', #程序exe的名称
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True, # 打包的时候进行压缩，False表示不压缩
          console=True, #此处console=True表示，打包后的可执行文件双击运行时屏幕会出现一个cmd窗口，不影响原程序运行，如不需要执行窗口，改成False即可。
          icon='C:\\Users\\Admin\\Desktop\\Tkinter\\1.ico') #程序图标，要绝对路径
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='test') #程序文件夹名称
 (3)通过pyinstaller打包spec文件
pyinstaller test.spec
此时项目下多了两个目录，进入dist目录，找到dist路径下后缀名为exe的文件。这里为dist下目录test下的test88.exe
注：如果要在其他电脑运行程序，需要把test整个文件夹拷贝过去。
————————————————
版权声明：本文为CSDN博主「檬柠wan」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qq_45664055/article/details/115659882'''