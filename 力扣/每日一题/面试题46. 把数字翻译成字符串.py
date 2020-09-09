class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)
        if len(num_str) <= 1:
            return 1
        # ans_lst = [0] * len(num_str)
        p = 1
        q = 2 if '25' >= num_str[0:2] >= '10' else 1 
        r = q
        # ans_lst[0] = 1
        # ans_lst[1] = 2 if '25' >= num_str[0:2] >= '10' else 1
        for i in range(2, len(num_str)):
            r = p + q if '25' >= num_str[i-1:i+1] >= '10' else q
            p, q = q, r
            # ans_lst[i] = ans_lst[i-1] + ans_lst[i-2] if '25' >= num_str[i-1:i+1] >= '10' else ans_lst[i-1]
        return r