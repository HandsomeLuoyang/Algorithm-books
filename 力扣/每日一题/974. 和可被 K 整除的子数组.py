class Solution:
    def subarraysDivByK(self, A: list, K: int) -> int:
        if len(A) == 1:
            return 1 if not A[0] % K else 0
        
        # # 这种前缀和的方式超时了
        # pre_sum = [A[0]]
        # tmp_sum = A[0]
        # for i in A[1:]:
        #     tmp_sum += i
        #     pre_sum.append(tmp_sum)

        # ans = 0
        # for i in pre_sum:
        #     if i % K == 0:
        #         ans += 1
        # for i in range(len(pre_sum)):
        #     for j in range(i + 1, len(pre_sum)):
        #         if (pre_sum[j] - pre_sum[i]) % K == 0:
        #             ans += 1
        # return ans

        pos = {}
        pos[0] = 1

        tmp_sum = 0
        for i in A:
            tmp_sum += i
            if (tmp_sum % K) in pos:
                pos[tmp_sum % K] += 1
            else:
                pos[tmp_sum % K] = 1
        
        ans = 0
        for k, v in pos.items():
            ans += v * (v - 1) // 2
        return ans


sol = Solution()
print(sol.subarraysDivByK([4, 5, 0, -2, -3, 1], 5))