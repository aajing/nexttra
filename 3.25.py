#cryto hw1
#3.25
#qiujing SA22221033

import numpy as np
from collections import Counter
from itertools import *
from scipy.stats import *
from operator import *

# 计算密文中字符的分布
def cipher2dist(cipher):

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher_text = cipher.replace(" ","").lower()

    cipher_freq = Counter(cipher_text)
    cipher_count = np.array([cipher_freq[i] for i in alphabet])
    cipher_dist = cipher_count / np.sum(cipher_count)

    return cipher_dist.tolist()

# 计算不同移位下的分布与标准分布间的距离并排序
def shift_sorted(cipher_dist, std_list, choose):

    cipher_iter = cycle(cipher_dist)

    chi2_list = []
    for i in range(26):
        chi2 = entropy(list(islice(cipher_iter, 26)), std_list)
        chi2_list.append((i, chi2))
        next(cipher_iter)

    return sorted(chi2_list, key = itemgetter(1))[:choose]

# 解密给定移位下的密文
def shift2plain(shift, cipher):

    cipher_text = cipher.replace(" ", "").lower()

    cipher_bytes = [ord(c) - ord('a') for c in cipher_text]
    plain_bytes = [chr((b - shift + 26) % 26 + ord('a')) for b in cipher_bytes]

    return "".join(plain_bytes)

# 标准分布
STD_FREQ = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702,
    0.02228, 0.02015, 0.06094, 0.06996, 0.00153,
    0.00772, 0.04025, 0.02406, 0.06749, 0.07507,
    0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 
    0.02758, 0.00978, 0.02360, 0.00150, 0.01974,
    0.00074
]

# 计算前10个最可能的结果
if __name__ == '__main__':

    cipher_txt = "phhwphdiwhuwkhwrjdsduwb"
    choose = 10

    cipher_dist = cipher2dist(cipher_txt)
    shifts, _ = zip(*shift_sorted(cipher_dist, STD_FREQ, choose))

    prob_plain = [shift2plain(s, cipher_txt) for s in shifts]
    
    for plain in prob_plain:
        print(plain)

# output:

# meetmeafterthetogaparty
# asshasothsfhvshcuodofhm
# tllatlhmalyaolavnhwhyaf
# bttibtpuitgiwtidvpepgin
# iaapiawbpanpdapkcwlwnpu
# zrrgzrnsgregurgbtncnegl
# kccrkcydrcprfcrmeynyprw
# phhwphdiwhuwkhwrjdsduwb
# gyyngyuznylnbyniaujulns
# woodwokpdobdrodyqkzkbdi

































