#! python3
#pw.py 口令保管箱

import sys,pyperclip

if len(sys.argv) < 2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()

passwords = {'QQ':'123456','wx':'153486','email':'m1616256collins'}

account = sys.argv[1] #命令行第一个参数是账户名

if account in passwords:
    pyperclip.copy(passwords[account])
    print(account + "密码已复制到剪贴板")
else:
    print("没有账户名叫" + account)