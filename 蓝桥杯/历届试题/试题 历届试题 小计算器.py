char_jinzhi = {chr(x): x-55 for x in range(65, 91)}
char_jinzhi.update({str(x):x for x in range(0, 10)})


def f(n, x):
    # n为待转换的十进制数，x为机制，取值为2-16
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'b', 'C', 'D', 'E', 'F']
    b = []
    while True:
        s = n//x  # 商
        y = n % x  # 余数
        b = b+[y]
        if s == 0:
            break
        n = s
    b.reverse()
    ss = ''
    for i in b:
        ss += str(a[i])
    return ss


zl_cnt = int(input())

cur_num = None
cur_jinzhi = 10
flag = None
for i in range(zl_cnt):
    zl = input()
    if zl == 'CLEAR':
        num = None
    elif zl.startswith('NUM'):
        tmp_num_str = zl.split(' ')[1]
        tmp_num = 0
        for i in range(len(tmp_num_str)):
            tmp_num += 10 ** (len(tmp_num_str) - i -1) * char_jinzhi[tmp_num_str[i]]
        tmp_num = int(str(tmp_num), base=cur_jinzhi)


        if flag:
            if flag == 'ADD':
                cur_num = cur_num + tmp_num
            elif flag == 'SUB':
                cur_num = cur_num - tmp_num
            elif flag == 'MUL':
                cur_num *= tmp_num
            elif flag == 'DIV':
                cur_num //= tmp_num
            elif flag == 'MOD':
                cur_num %= tmp_num
            flag = None
        else:
            cur_num = tmp_num
    elif zl in ['ADD', 'SUB', 'MUL', 'DIV', 'MOD']:
        flag = zl
    elif zl.startswith('CHANGE'):
        try:
            cur_jinzhi = int(zl.split(' ')[1])
        except:
            cur_jinzhi = char_jinzhi[zl.split(' ')[1]]
    elif zl == 'EQUAL':
        print(f(cur_num, cur_jinzhi))
    elif zl == 'CLEAR':
        pass
