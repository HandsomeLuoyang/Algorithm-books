ss = """4 0 4 0 4 0 4 32 -1 -16 4 32 4 32 4 32 4 32 4 32 8 32 8 32 16 34 16 34 32 30 -64 0
16 64 16 64 34 68 127 126 66 -124 67 4 66 4 66 -124 126 100 66 36 66 4 66 4 66 4 126 4 66 40 0 16
4 0 4 0 4 0 4 32 -1 -16 4 32 4 32 4 32 4 32 4 32 8 32 8 32 16 34 16 34 32 30 -64 0
0 -128 64 -128 48 -128 17 8 1 -4 2 8 8 80 16 64 32 64 -32 64 32 -96 32 -96 33 16 34 8 36 14 40 4
4 0 3 0 1 0 0 4 -1 -2 4 0 4 16 7 -8 4 16 4 16 4 16 8 16 8 16 16 16 32 -96 64 64
16 64 20 72 62 -4 73 32 5 16 1 0 63 -8 1 0 -1 -2 0 64 0 80 63 -8 8 64 4 64 1 64 0 -128
0 16 63 -8 1 0 1 0 1 0 1 4 -1 -2 1 0 1 0 1 0 1 0 1 0 1 0 1 0 5 0 2 0
2 0 2 0 7 -16 8 32 24 64 37 -128 2 -128 12 -128 113 -4 2 8 12 16 18 32 33 -64 1 0 14 0 112 0
1 0 1 0 1 0 9 32 9 16 17 12 17 4 33 16 65 16 1 32 1 64 0 -128 1 0 2 0 12 0 112 0
0 0 0 0 7 -16 24 24 48 12 56 12 0 56 0 -32 0 -64 0 -128 0 0 0 0 1 -128 3 -64 1 -128 0 0"""

splited_ss = ss.split('\n')

for line_ss in splited_ss:
    line_int = list(map(lambda x:int(x), line_ss.split(' ')))
    for i in range(0, 32, 2):
        left_num, right_num = line_int[i], line_int[i+1]
        left_bin = list(str(bin(left_num)).replace('0b', '').replace('-', ''))
        if left_num < 0:
            for j in range(len(left_bin)-1, -1, -1):
                if left_bin[j] == '1':
                    for k in range(0, j):
                        if left_bin[k] == '0':
                            left_bin[k] = '1'
                        else:
                            left_bin[k] = '0'
                    break
        left_bin = ''.join(left_bin)
        left_bin_length = len(left_bin)
        left_bin = (8-left_bin_length) * '0' + left_bin

        right_bin = list(str(bin(right_num)).replace('0b', ''))
        if right_num < 0:
            for j in range(len(right_bin)-1, -1, -1):
                if right_bin[j] == '1':
                    for k in range(0, j):
                        if right_bin[k] == '0':
                            right_bin[k] = '1'
                        else:
                            right_bin[k] = '0'
                    break
        right_bin = ''.join(right_bin)
        right_bin_length = len(right_bin)
        right_bin = (8-right_bin_length) * '0' + right_bin

        print_ss = left_bin + right_bin
        for i in print_ss:
            if i == '1':
                print(i, end='')
            else :
                print(' ', end='')
        print()
    

    print('=' * 30)
