'''
借鉴《Python编程 从入门到实践》第18章内容，在安装运行Django前增设虚拟环境安装激活

建立虚拟环境：
为新项目新建一个目录，如<learning_log>，在终端中cd至该目录下
（如我的是在D：\learning_log）
D：
cd learning_log
运行模块venv，创建虚拟环境,环境名为<11_env>
python -m venv 11_env
查看本地文件夹，发现文件夹内增加了一些文件

激活虚拟环境：
source 11_env/bin/activate
我的是win10，使用下面的代码来激活虚拟环境
11_env\Scripts\activate (不包含source)
这时PowerShell提示我：无法加载文件 D:\learning_log\11_env\Scripts\Activate.ps1，因为在此系统上禁止运行脚本。
使用指令 set-ExecutionPolicy RemoteSigned 对执行策略进行更改
执行策略更改
执行策略可帮助你防止执行不信任的脚本。更改执行策略可能会产生安全风险，如 https:/go.microsoft.com/fwlink/?LinkID=135170
中的 about_Execution_Policies 帮助主题所述。是否要更改执行策略?
[Y] 是(Y)  [A] 全是(A)  [N] 否(N)  [L] 全否(L)  [S] 暂停(S)  [?] 帮助 (默认值为“N”): Y
这里我输入了Y，再次输入指令 11_env\Scripts\activate
PS D:\learning_log> 11_env\Scripts\activate
虚拟环境成功启用：
(11_env) PS D:\learning_log>

停用虚拟环境，可执行命令 deactivate
(11_env) PS D:\learning_log> deactivate
PS D:\learning_log>
或者直接关闭运行虚拟环境的终端，虚拟环境也将不再处于活动状态

'''
