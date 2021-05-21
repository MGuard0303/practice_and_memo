"""docstrings

本文件定义了一个将文本独热编码 (one-hot encoding) 的函数。

# ==========
# 注意：这只是该函数的初期版本，功能尚未完善。
# ==========

这个函数接受一个字符串 (DNA/RNA 序列) 为输入。当前版本只考虑将纯序列作为输入，没有考虑各种序列格式的处理和转换。

该函数使用 sklearn.preprocessing.LabelEncoder() 将序列转换为 integer encoding 的形式，然后使用 PyTorch 自带的 one_hot() 函数将 integer encoding 序列转换为独热编码形式。
"""



import numpy as np 
import torch
from torch.nn import functional as F 
from sklearn import preprocessing


def one_hot_encode(sequence):
    label_encoder = preprocessing.LabelEncoder()

    seq_array = np.array(list(sequence))

    # 序列的integer encoding形式
    integer_encoding = label_encoder.fit_transform(seq_array)

    # 将integer encoding的序列转化为pytorch tensor
    seq_tensor = torch.tensor(integer_encoding)

    # 使用pytorch的方法生成one-hot encoding
    one_hot_seq = F.one_hot(seq_tensor)


    return one_hot_seq



# e.g.
example = "UACCUGGUUGAUCCUGCCAGUAGCAUAUGCUUGUCUC"
one_hot_example = one_hot_encode(example)
print(one_hot_example)