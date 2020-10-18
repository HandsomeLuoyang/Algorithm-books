import collections
from typing import *


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        return list(reduce(lambda x, y: x & y, map(collections.Counter, A)).elements())