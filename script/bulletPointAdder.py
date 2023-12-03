#! python3
# 在每行文本前添加星号和空格复制到剪贴板

import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pyperclip.copy(text)

