# Spelling Correction

这是蓝猫的 Spelling Correction 应用。

## 依赖

该应用依赖 venv，torch，transformers 和 nltk 这四个库，以及 `oliverguhr/spelling-correction-english-base` 模型和 `nltk` 用到的模型和数据集。请您安装 `venv`，以方便我的脚本创建虚拟环境，防止该项目的依赖破坏您的主要 python 环境。其它依赖您不需要手动安装，我的脚本会帮您安装。

### 如何安装 venv ？

在 windows 和 debian/ubuntu 上安装 venv 的方法如下：

- 在 windows 上，你需要先安装 pip，一个 python 的包管理器。你可以使用以下命令来检查和更新 pip：

```bash
py -m pip --version # 查看 pip 的版本
py -m pip install --upgrade pip # 更新 pip 到最新版本
```

- 然后，你可以使用 pip 来安装 venv，一个用于创建虚拟环境的模块。你可以使用以下命令来安装 venv：

```bash
py -m pip install --user virtualenv # 安装 venv 到用户目录
```

- 在 debian 上，你需要安装 python3.x-venv，`.x` 指您具体的 python 版本，例如 `python3.10-venv`。你可以使用以下命令来安装 python3.x-venv：

```bash
sudo apt update # 更新软件源
sudo apt install python3.x-venv # 安装 python3 和 python3.x-venv
```

## 运行

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

## 注意事项

我在代码里设置的模型可接收的最大长度是 4096。如果您需要处理更长的文本，可以修改 `run.ps1` 中的 `$max_length = 4096` 的值，如果您是 Linux 用户，可以修改 `run.sh` 中的 `max_length=4096` 的值。

## 原理介绍

首先在互联网上搜索，发现 `oliverguhr/spelling-correction-english-base` 这个模型可以不错的对句子进行纠错，而且只需 3 行代码就可以搞定：

```python
from transformers import pipeline

fix_spelling = pipeline("text2text-generation",model="oliverguhr/spelling-correction-english-base")

print(fix_spelling("lets do a comparsion", max_length=4096))
```

但是经过测试，一旦输入的句子过长，该模型就会胡言乱语。

所以我引入了 `nltk`，另一个 NLP 模型，用来把用户的输入按句来分开，然后分别让 `oliverguhr/spelling-correction-english-base` 纠错，最终再拼接到一起：

```python
 # split the input into sentences
sentences = nltk.sent_tokenize(line)
# initialize an empty list to store the corrected sentences
corrected_sentences = []
# loop over each sentence and correct it
for sentence in sentences:
    result = fix_spelling(sentence, max_length=max_length)
    corrected_sentences.append(result[0]["generated_text"])
# join the corrected sentences with a space
output = " ".join(corrected_sentences)
print("===========================================")
print("result: " + output)
```
