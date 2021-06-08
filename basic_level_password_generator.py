"""docstring
这个类使用 secrets 模块产生随机密码。可以指定密码是否包含大写字符，是否包含标点符号。

生成的密码可以保存在一个文件内。


# ==========
# Future work
# 完成对已保存密码的管理 (比较，删除等)
# ==========
"""


import string
import secrets
import os


LOWERCASE = string.ascii_lowercase + string.digits
LETTER = string.ascii_letters + string.digits
PUNC = string.punctuation


class PasswordGenerator():
    def __init__(self) -> None:
        self.pwd = ""


    def generate(self, length, uppercase=None, upper_n=None, punc=False, punc_n=None):
        if length < 8:
            raise ValueError("The length of password should longer than 8")

        # condition 1
        if uppercase == True and punc == False:
            if upper_n != None:
                while True:
                    temp_pwd = "".join(secrets.choice(LETTER) for i in range(length))

                    if sum(char.isupper() for char in temp_pwd) >= upper_n and any(char.isdigit() for char in temp_pwd):
                        self.pwd = temp_pwd
                        return self.pwd
                        break

            elif upper_n == None:
                raise TypeError("Parameter 'upper_n' should be an int.")

        # condition 2
        if uppercase == True and punc == True:
            if punc_n != None:
                while True:
                    temp_pwd = "".join(secrets.choice(LETTER + PUNC) for i in range(length))

                    if sum(char.isupper() for char in temp_pwd) >= upper_n and sum(char in PUNC for char in temp_pwd) >= punc_n and any(char.isdigit() for char in temp_pwd):
                        self.pwd = temp_pwd
                        return self.pwd
                        break
            
            elif upper_n == None or punc_n == None:
                raise TypeError("Parameter 'upper_n' and parameter 'punc_c' should be an int.")


        # condition 3
        if uppercase == False and punc == False:
            while True:
                temp_pwd = "".join(secrets.choice(LOWERCASE) for i in range(length))

                if any(char.isdigit() for char in temp_pwd):
                    self.pwd = temp_pwd
                    return self.pwd
                    break

        
        # condition 4
        if uppercase == False and punc == True:
            if punc_n != None:
                while True:
                    temp_pwd = "".join(secrets.choice(LOWERCASE + PUNC) for i in range(length))

                    if any(char.isdigit() for char in temp_pwd) and any(char in PUNC for char in temp_pwd):
                        self.pwd = temp_pwd
                        return self.pwd
                        break
            
            elif punc_n == None:
                raise TypeError("Parameter 'punc_n' should be an int.")


    
    def clear(self):
        self.pwd = ""



    # 将生成的密码存储在一个文件内
    def save(self, path, filename):
        # 如果传入的path尚未建立，先建立这个路径
        if os.path.isdir(path) == False:
            os.makedirs(path)

        
        with open(os.path.join(path, filename), "a") as f:
            f.write(self.pwd)
            print("Password has been saved.")
            self.clear()


    # 需要实现对存有密码的文件的管理


                
                    
