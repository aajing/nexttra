#cryto hw1
#3.28
#qiujing SA22221033

import copy
import numpy as np

# 编写计算模p下的高斯消元法
class hill_cipher:
    def __init__(self, K):
        self.K = K

    @staticmethod
    def mod_gauss(a, b, p):
        
        mat = copy.deepcopy(a)
        y = copy.deepcopy(b)
        m, n = len(b), len(a)

        for k in range(0, n-1):
            for i in range(k+1, n):
                z = mat[i][k] * pow(mat[k][k], -1, p) % p
                for l in range(m):
                    y[l][i] = (y[l][i] - z * y[l][k]) % p
                mat[i][k] = 0
                for j in range(k+1, n):
                    mat[i][j] = (mat[i][j] - z * mat[k][j]) % p

        x = [[0 for _ in range(n)] for _ in range(m)]

        for l in range(m):
            for i in range(n-1, -1, -1):
                s = 0
                for j in range(i+1, n):
                    s = (s + mat[i][j] * x[l][j]) % p
                x[l][i] = (y[l][i] - s) * pow(mat[i][i], -1, p) % p

        return x

# 编写解密函数
    def enc(self, plain_txt):
        return np.mod(np.matmul(np.array(self.K, dtype=int), np.array(plain_txt, dtype=int)), 26).tolist()

    def dec(self, cipher_txt):
        return self.mod_gauss(self.K, [cipher_txt], 26)[0]

    def __repr__(self) -> str:
        return "{}".format(self.K)

    def __eq__(self, __o: object) -> bool:
        return self.K == __o.K

# 通过已知明文攻击破解hill密码
# 只需要一次gauss消元法就可以解出K
def hill_atk(plains, ciphers):

    assert len(plains) == len(plains[0])

    cipher_vecs = (np.array(ciphers).T).tolist()
    recovered_K = hill_cipher.mod_gauss(plains, cipher_vecs, 26)

    return hill_cipher(recovered_K)

# 示例
if __name__ == '__main__':
    hill = hill_cipher([[17,17,5],
                        [21,18,21],
                        [2,2,19]])
    
    plain_txt = [[15,0,24],
                 [18,19,17],
                 [5,12,15]]
    assert np.linalg.matrix_rank(plain_txt) == 3

    cipher_txt = [hill.enc(pt) for pt in plain_txt]

    recovered_hill = hill_atk(plain_txt, cipher_txt)
    print(recovered_hill == hill)

# output:
# True