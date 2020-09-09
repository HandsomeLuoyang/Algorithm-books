from collections import Counter
class Solution():
    def findSubstring(self, s: str, words: list) -> list:
        # 动态规划+哈希试试
        if len(s) == 0 or len(words) == 0:
            return []
        word_length = len(words[0])
        words_numbers = len(words)
        ans_lst = []
        c = Counter(words)
        hash_dict = dict(c)
        # for word in words:
        #     if not word in hash_dict:
        #         hash_dict[word] = words.count(word)
        s_length = len(s)

        # 当前前指针的位置`
        cur_position = 0
        # 出现了的单词的数量
        cnt = 0
        # 临时字典，验证
        tmp_dict = {}
        # 当前记录着的可能是出现位置的索引
        now_index = -1
        while True:
            if cur_position + word_length > s_length:
                return ans_lst
            tmp_s = s[cur_position:cur_position+word_length] 

            if not tmp_s in hash_dict:
                # 代表匹配了前面一部分，但是后面匹配失败了，要从记录的的index+1继续匹配
                if tmp_dict:
                    tmp_dict = {}
                    cur_position = now_index + 1
                    cnt = 0
                    continue
                
                cur_position += 1
                tmp_dict = {}
                cnt = 0

            else:
                # 这里代表当前这个单词匹配成功了
                if not tmp_dict:
                    # 如果这个单词是新匹配的，也就是一串的第一个单词，就把这个index记录
                    now_index = cur_position
                
                if tmp_s not in tmp_dict:
                    # 如果这个匹配成功的单词在这一串中还没匹配过，就给它在字典中创建出来
                    tmp_dict[tmp_s] = 1
                    cnt += 1
                    # 如果当前匹配成功的单词数量已经达到了给定数量，代表成功匹配了，放入index，重新回到index+1继续匹配
                    if cnt == words_numbers:
                        ans_lst.append(now_index)
                        cnt = 0
                        tmp_dict = {}
                        cur_position = now_index + 1
                        now_index = -1
                        continue
                    # 如果还没有到达数量，就跳过等间距的下一个单词去匹配
                    cur_position += word_length
                    
                else:
                    # 如果当前单词已经出现过限定次数了，就代表上一串匹配失败
                    if tmp_dict[tmp_s] == hash_dict[tmp_s]:
                        tmp_dict = {}
                        cur_position = now_index+1
                        cnt = 0
                    # 如果当前单词还没到达限定次数，就继续匹配下去
                    else:
                        tmp_dict[tmp_s] += 1
                        cnt += 1
                        if cnt == words_numbers:
                            ans_lst.append(now_index)
                            cnt = 0
                            tmp_dict = {}
                            cur_position = now_index + 1
                            now_index = -1
                            continue
                        cur_position += word_length

        # print(hash_dict)


s = Solution()
print(s.findSubstring('barfoofoobarthefoobarman',
                words=["bar","foo","the"]))
