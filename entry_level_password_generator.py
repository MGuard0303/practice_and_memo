"""docstring
# ==========
# DEPRECATED
# This class will not be updated and used any more.
# ==========


这里定义了一个用于生成随机密码的类。参数 pass_len, capital, punc 分别控制密码的长度，是否需要大写字符和是否需要标点符号。

密码的前8位通过定义好的规则生成。当前版本8位之后的密码是随机的小写字符，但是更改也很容易。密码在返回用户时会被打乱。


# ==========
# Note: 最好使用 secrets 模块代替 random 模块
# ==========


# ==========
# Future Work
# 1. 当 pass_len 小于8时构造失败，并返回提示。
# 2. 将密码保存在一个密码本中，并维护这个密码本。
# ==========
"""


import string
import random



LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
NUMBER = string.digits
PUNCTUATION = string.punctuation


class PasswordGenerator(): 
    # 尚未实现密码长度小于8时构造失败
    def __init__(self, pass_len=8, capital=True, punc=False) -> None:
        self.pass_len = pass_len
        self.capital = capital
        self.punc = punc
        self.pwd = []


    def generate(self):
        # condition 1
        if self.capital == True and self.punc == False:
            [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in (0, 1, 2, 3)] # 也可以使用random或secrets模块的choice()函数简单实现
            [self.pwd.append(UPPERCASE[random.randint(0, len(UPPERCASE)-1)]) for i in (4, 5)]
            [self.pwd.append(NUMBER[random.randint(0, len(NUMBER)-1)]) for i in (6, 7)]

            if len(self.pwd) < self.pass_len:
                [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in range(8, self.pass_len)]
            
            random.shuffle(self.pwd)
            password = "".join(self.pwd)
            return password
        
        
        """
        另一种实现方式是指定特殊符号 ( 大写字符，数字，标点符号等 ) 的数量，使用 while True 无限循环不断生成随机字符串，通过 any(), sum() 等函数检查字符串是否包含指定种类指定数量的特殊符号。
        """


        # condition 2
        if self.capital == True and self.punc == True:
            [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in (0, 1, 2)]
            [self.pwd.append(UPPERCASE[random.randint(0, len(UPPERCASE)-1)]) for i in (3, 4)]
            [self.pwd.append(NUMBER[random.randint(0, len(NUMBER)-1)]) for i in (5, 6)]
            self.pwd.append(PUNCTUATION[random.randint(0, len(PUNCTUATION)-1)])

            if len(self.pwd) < self.pass_len:
                [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in range(8, self.pass_len)]
            
            random.shuffle(self.pwd)
            password = "".join(self.pwd)
            return password


        # condition 3
        if self.capital == False and self.punc == False:
            [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in (0, 1, 2, 3)]
            [self.pwd.append(NUMBER[random.randint(0, len(NUMBER)-1)]) for i in (4, 5, 6, 7)]

            if len(self.pwd) < self.pass_len:
                [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in range(8, self.pass_len)]
            
            random.shuffle(self.pwd)
            password = "".join(self.pwd)
            return password


        # condition 4
        if self.capital == False and self.punc == True:
            [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in (0, 1, 2, 3)]
            [self.pwd.append(NUMBER[random.randint(0, len(NUMBER)-1)]) for i in (4, 5, 6)]
            self.pwd.append(PUNCTUATION[random.randint(0, len(PUNCTUATION)-1)])

            if len(self.pwd) < self.pass_len:
                [self.pwd.append(LOWERCASE[random.randint(0, len(LOWERCASE)-1)]) for i in range(8, self.pass_len)]
            
            random.shuffle(self.pwd)
            password = "".join(self.pwd)
            return password


    def clear(self):
        self.pwd = []


    def reset(self):
        self.pass_len = 8
        self.capital = True
        self.punc = False
        self.pwd = []


# 可选功能：将密码保存在一个codebook中并维护这个codebook
