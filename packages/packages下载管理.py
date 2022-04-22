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