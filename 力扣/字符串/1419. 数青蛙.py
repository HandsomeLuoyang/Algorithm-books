class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        val_dict = {'p': float('inf'), 'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
        last_dict = {'c': 'p', 'r': 'c', 'o': 'r', 'a': 'o', 'k': 'a'}
        frogs = 0
        for i in croakOfFrogs:
            val_dict[i] += 1
            if val_dict[i] > val_dict[last_dict[i]]:
                return -1
            if i == 'k':
                val_dict['c'] -= 1
                val_dict['r'] -= 1
                val_dict['o'] -= 1
                val_dict['a'] -= 1
                val_dict['k'] -= 1

            frogs = max(frogs, val_dict['c'])
        if val_dict['c'] != 0:
            return -1
        return frogs