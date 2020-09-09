import traceback

row, col = [int(x) for x in input().split()]
area = row * col
k = int(input())
big_list = list()
visited = set()
visited = {}

cur_index = 0
try:
    for i in range(k):
        left, right = [int(x) for x in input().split()]
        if left == 439:
            print('hah')
        if not left in visited and not right in visited:
            tmp_set = set()
            tmp_set.add(left)
            tmp_set.add(right)
            big_list.append(tmp_set)
            # visited.add(left)
            # visited.add(right)
            visited[left] = cur_index
            visited[right] = cur_index
            cur_index += 1
        elif left in visited and not right in visited:
            # for j in range(len(big_list)):
            #     if left in big_list[j]:
            #         big_list[j].add(right)
            #         break
            big_list[visited[left]].add(right)
            visited[right] = visited[left]
            # visited.add(right)
        elif not left in visited and right in visited:
            # for j in range(len(big_list)):
            #     if right in big_list[j]:
            #         big_list[j].add(left)
            #         break
            # visited.add(left)
            big_list[visited[right]].add(left)
            visited[left] = visited[right]
        elif left in visited and right in visited:
            # left_set_index, right_set_index = -1, -1
            # for j in range(len(big_list)):
            #     if left in big_list[j]:
            #         left_set_index = j
            #     if right in big_list[j]:
            #         right_set_index = j
            # if left_set_index != right_set_index:
            #     big_list.append(big_list[left_set_index].union(big_list[right_set_index]))
            #     big_list.remove(big_list[left_set_index])
            #     big_list.remove(big_list[right_set_index])
            if visited[left] != visited[right]:
                big_list[visited[left]] = big_list[visited[left]].union(big_list[visited[right]])
                for j in big_list[visited[right]]:
                    visited[j] = visited[left]
                big_list.pop(visited[right])
                cur_index -= 1
        # print(big_list)
        # print(cur_index)
        # print(visited)
except Exception as e:
    traceback.print_exc(file=open('a.txt', 'w'))
    


print(len(big_list) + area - len(visited))

