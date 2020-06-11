class Solution:
    # 暴力方法
#     def numPairsDivisibleBy60(self, time:list) -> int:
#         ans = 0
#         length = len(time)
#         for i in range(length):
#             for j in range(i+1, length):
#                 if (time[i] + time[j]) % 60 == 0:
#                     ans += 1
#         return ans

    # 余数法
#     def numPairsDivisibleBy60(self, time:list) -> int:
#         ans = 0
#         time = [i%60 for i in time]
#         st = time.process_time()
#         for i in range(0, 30):
#             tmp = 60 - i
#             ans += time.count(i) * time.count(tmp)
#         ed = time.process_time()
#         print(ed-st)
#         num_60 = time.count(0)
#         ans += (num_60 * (num_60-1)) // 2 
#         num_30 = time.count(30)
#         ans += (num_30 * (num_30-1)) // 2
#         return ans

    def numPairsDivisibleBy60(self, time:list) -> int:
        dic = {}
        ans = 0
        for i in time:
            i = i % 60
            tmp = (60-i) % 60
            if tmp in dic:
                ans += dic[tmp]
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        return ans