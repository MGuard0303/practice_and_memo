"""docstring

# ==========
# Note: 目前尚未在 macOS 系统中测试
# ==========
"""


import shutil
import os
import datetime


while True:
    source = input("Please enter full path of directory you want to archive:")  # 返回 str
   
    if source == "exit":
        exit()
    
    elif os.path.isdir(source) == False or os.path.exists(source) == False:
        print("Please enter a valid path.")
        continue

    
    target = input("Please enter where you want to preserve the archive file (path or file name):")
    current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M")


    if os.path.isdir(target) == True: 
        file_name = target + "/archive_" + current_time  # 为归档文件给予默认名 archive
    elif os.path.isdir(target) == False:
        file_name = source + "/" + target + "_" + current_time  # 如果未给出压缩包路径，默认路径在需要压缩的路径下
    

    # 归档使用 shutil.make_archive() 函数
    shutil.make_archive(base_name=file_name, format="zip", root_dir=source)
    print("Archive success")
    break
