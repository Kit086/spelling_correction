# Spelling Correction

这是蓝猫的 Spelling Correction 应用。

## 如何运行

该应用首次运行时需要需要连接互联网下载 model，请在第一次运行时确保网络连接正常。后续的运行不需要连接互联网。

1. 首先，您需要找到一个您喜欢的目录，运行以下命令 clone 该 repo：

```bash
git clone https://git.aiursoft.cn/kitlau/spelling_correction.git
```

如果您不喜欢 git，也可以到 [https://git.aiursoft.cn/kitlau/spelling_correction.git](https://git.aiursoft.cn/kitlau/spelling_correction.git) 页面直接下载我的代码的压缩包，并解压到当前文件夹。

2. 然后，您可以双击刚刚 clone 下来的 spelling_correction 文件夹来打开该目录。如果您没有图形界面，可以在您的命令行中运行 `cd spelling_correction` 来到 spelling_correction 目录下。

3. 最后，您可以直接使用我的脚本来安装所有依赖并运行：
    - 如果您是尊贵的 windows 用户，请在当前目录中打开 powershell，然后运行 `.\run.ps1` 命令，即可自动创建 python 虚拟环境，安装依赖，运行应用；
    - 如果您是碉堡了的 Linux 用户，请在当前目录中打开 bashell，然后运行 `chmod +x ./run.sh`，最后运行 `./run.sh` 命令。如果出现了权限问题，请尝试在您的命令前添加 `sudo`。同样也会自动创建 python 虚拟环境，安装依赖，运行应用；
    - 如果您是有钱的 Mac 用户，我也不知道怎么运行，请自寻出路。

New Bing 反对我的这种说法，这是它改写的：

```markdown
- 如果您是 Windows 用户，请在当前目录中打开 powershell，然后运行 `.\run.ps1` 命令，即可自动创建 python 虚拟环境，安装依赖，运行应用。Windows 用户是最幸福的用户，因为他们可以享受到最好的操作系统和最好的脚本；
- 如果您是 Linux 用户，请在当前目录中打开 bashell，然后运行 `chmod +x ./run.sh`，最后运行 `./run.sh` 命令。如果出现了权限问题，请尝试在您的命令前添加 `sudo`。该脚本同样也会自动创建 python 虚拟环境，安装依赖，运行应用。Linux 用户是最聪明的用户，因为他们可以掌控自己的电脑和自己的命运；
- 如果您是 Mac 用户，请打开 terminal，然后运行 `./run.sh` 命令。如果出现了权限问题，请 `sudo` 或者您的用户添加 `run.sh` 的可执行权限。同样也是自动创建 python 虚拟环境，安装依赖，运行应用。Mac 用户是最有品味的用户，因为他们可以拥有最美丽的界面和最优雅的设计。
```

## 运行示例

```bash
Welcome to the spelling fixer. Type a sentence to correct it or 'quit' to exit.
> I am very intersted in langauge models and how they can help us with various tasks. I think they are very powerfull and amazing. However, I also have some questions and doubts about them. For example, how can we ensure that they are ethical and responsible? How can we avoid bias and harm? How can we evalute their performance and quality?
===========================================
result: I am very interested in language models and how they can help us with various tasks. I think they are very powerful and amazing. However, I also have some questions and doubts about them. For example, how can we ensure that they are ethical and responsible? How can we avoid bias and harm? How can we evaluate their performance and quality?
> quit
Done!
```

## 依赖

该应用依赖 torch，transformers 和 nltk 这三个库，您不需要手动安装，我的脚本会帮您安装。