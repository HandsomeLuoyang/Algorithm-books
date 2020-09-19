matrix_9 = ''
for i in range(3):
    matrix_9 += ''.join(input().split())

ans_strs = ["816357492","618753294","492357816","294753618","672159834","834159672","276951438","438951276"]

ans_num = 0
first_ans_str = ''
flag = False
for one_ans in ans_strs:
    for i in range(len(one_ans)):
        if matrix_9[i] != '0' and one_ans[i] != matrix_9[i]:
            break
        if (matrix_9[i] == one_ans[i] or matrix_9[i] == '0') and i == 8:
            flag = True
    if flag:
        if ans_num == 0:
            first_ans_str = one_ans[:]
            ans_num = 1
            flag = False
        else:
            print('Too Many')
            exit(0)

print(first_ans_str[0], first_ans_str[1], first_ans_str[2])
print(first_ans_str[3], first_ans_str[4], first_ans_str[5])
print(first_ans_str[6], first_ans_str[7], first_ans_str[8])