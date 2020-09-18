ss = ''
while True:
    s = input()
    ss += s
    if 'E' in s:
        break

E_index = ss.index('E')
w_n = 0
l_n = 0

for i in range(E_index):
    if ss[i] == 'W':
        w_n += 1
    elif ss[i] == 'L':
        l_n += 1
    if w_n >= 11 or l_n >= 11:
        if abs(w_n-l_n) < 2:
            continue
        print('{}:{}'.format(w_n, l_n))
        w_n = 0
        l_n = 0
print('{}:{}'.format(w_n, l_n))
print('')

w_n = 0
l_n = 0

for i in range(E_index):
    if ss[i] == 'W':
        w_n += 1
    elif ss[i] == 'L':
        l_n += 1
    if w_n >= 21 or l_n >= 21:
        if abs(w_n-l_n) < 2:
            continue
        print('{}:{}'.format(w_n, l_n))
        w_n = 0
        l_n = 0
print('{}:{}'.format(w_n, l_n))
