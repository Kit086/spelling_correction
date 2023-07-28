# Spelling Correction

这是蓝猫的 Spelling Correction 应用。

## 如何运行

该应用首次运行时需要需要连接互联网下载 model，请在第一次运行时确保网络连接正常。后续的运行不需要连接互联网。

- 如果您是尊贵的 windows 用户，请打开 powershell，然后运行 `.\run.ps1\` 命令，即可自动创建 python 虚拟环境，安装依赖，运行应用；
- 如果您是朴素的 Linux 用户，请打开 bashell，然后运行 `./run.sh` 命令。如果出现了权限问题，请运行 `sudo ./run.sh`。同样也是自动创建 python 虚拟环境，安装依赖，运行应用；
- 如果您是卑贱的 Mac 用户，我也不知道怎么运行，请自寻出路。

New Bing 反对我的这种说法，这是它改写的：

```markdown
- 如果您是 Windows 用户，请打开 powershell，然后运行 `.\run.ps1` 命令，即可自动创建 python 虚拟环境，安装依赖，运行应用。Windows 用户是最幸福的用户，因为他们可以享受到最好的操作系统和最好的脚本；
- 如果您是 Linux 用户，请打开 bashell，然后运行 `./run.sh` 命令。如果出现了权限问题，请运行 `sudo ./run.sh`。同样也是自动创建 python 虚拟环境，安装依赖，运行应用。Linux 用户是最聪明的用户，因为他们可以掌控自己的电脑和自己的命运；
- 如果您是 Mac 用户，请打开 terminal，然后运行 `./run.sh` 命令。如果出现了权限问题，请运行 `sudo ./run.sh`。同样也是自动创建 python 虚拟环境，安装依赖，运行应用。Mac 用户是最有品味的用户，因为他们可以拥有最美丽的界面和最优雅的设计。
```

## 依赖

该应用依赖 torch，transformers 和 nltk 这三个库，您不需要手动安装，我的脚本会帮您安装。