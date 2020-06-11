class Solution:
    def equationsPossible(self, equations: list) -> bool:
        self.set_list = []
        for s in equations:
            # 获得两个变量所在集合
            index1, index2 = self.get_union_index(s[0]), self.get_union_index(s[-1])
            # 如果等式需要这两个变量在同一个集合
            if s[1] == '=':
                # 已经在同一个集合
                if index1 != -1 and index1 == index2:
                    continue
                # 有一个在集合中，另一个不在
                elif index1 != -1 and index2 == -1:
                    self.set_list[index1].add(s[-1])
                elif index2 != -1 and index1 == -1:
                    self.set_list[index2].add(s[0])
                # 都不在集合中
                elif index1 == -1 and index2 == -1:
                    new_set = set()
                    new_set.add(s[0])
                    new_set.add(s[-1])
                    self.set_list.append(new_set)
                # 在不同集合中
                else:
                    # 可以合并就合并
                    len_set1, len_set2 = len(self.set_list[index1]), len(self.set_list[index2])
                    new_set = self.set_list[index1] | self.set_list[index2]
                    if len(new_set) == len_set1 + len_set2:
                        self.set_list.pop(index1)
                        if index1 < index2:
                            self.set_list.pop(index2-1)
                        else:
                            self.set_list.pop(index2)
                        self.set_list.append(new_set)
                    # 不可以合并就返回False
                    else:
                        return False
            # 如果等式需要两个变量在不同集合
            else:
                # 已经在不同集合
                if index1 != -1 and index2 != -1 and index1 != index2:
                    continue
                # 一个在集合中，另一个不在
                elif index1 != -1 and index2 == -1:
                    new_set = set()
                    new_set.add(s[-1])
                    self.set_list.append(new_set)
                elif index2 != -1 and index1 == -1:
                    new_set = set()
                    new_set.add(s[0])
                    self.set_list.append(new_set)
                # 在相同集合中
                elif index1 != -1 and index1 == index2:
                    return False
                # 两个都不在集合中
                else:
                    new_set1 = set()
                    new_set1.add(s[-1])
                    self.set_list.append(new_set1)
                    new_set2 = set()
                    new_set2.add(s[0])
                    self.set_list.append(new_set2)

        # 第二次检验，因为第一次遍历的时候，如果相同的元素在不同集合中可能会误合并，这里再来判断一次，就没问题了
        for s in equations:
            # 获得两个变量所在集合
            index1, index2 = self.get_union_index(s[0]), self.get_union_index(s[-1])
            # 如果两个需要在不同集合的在了同一个集合，返回错误
            if s[1] == '!':
                if index1 == index2:
                    return False

        return True

    def get_union_index(self, s) -> int:
        for i, v in enumerate(self.set_list):
            if s in v:
                return i
        return -1

sol = Solution()
print(sol.equationsPossible(["a==b","e==c","b==c","a!=e"]))