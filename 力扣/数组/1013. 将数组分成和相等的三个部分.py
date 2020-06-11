class Solution:
    def canThreePartsEqualSum(self, A: list) -> bool:
        if len(A) < 3 or sum(A) % 3 != 0:
            return False
        one_three = sum(A) // 3
        tmp_sum = 0
        
        tag = 0
        for i in range(0, len(A)):
            tmp_sum += A[i]
            if tmp_sum == one_three:
                tmp_sum = 0
                tag += 1
                if tag == 3:
                    return True
        
        return False