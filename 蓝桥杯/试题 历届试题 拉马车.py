A_str = list(input())
B_str = list(input())
dachu = []

while A_str and B_str:
    while True:
        char = A_str.pop(0)
        if dachu.count(char) == 1:
            start_index = dachu.index(char)
            dachu.append(char)
            A_str.extend(dachu[start_index:][::-1])
            dachu = dachu[:start_index]
        else:
            if not A_str:
                print(''.join(B_str))
                exit(0)
            dachu.append(char)
            break

    while True:
        char = B_str.pop(0)
        if dachu.count(char) == 1:
            start_index = dachu.index(char)
            dachu.append(char)
            B_str.extend(dachu[start_index:][::-1])
            dachu = dachu[:start_index]
        else:
            dachu.append(char)
            break
    
print(''.join(A_str) if A_str else ''.join(B_str))