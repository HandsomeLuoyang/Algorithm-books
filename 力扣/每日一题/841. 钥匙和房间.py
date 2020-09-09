class Solution:
    def canVisitAllRooms(self, rooms: list) -> bool:
        if len(rooms) < 1:
            return False
        room_cnt = len(rooms)
        ans_set = set()

        def dfs(n):
            if n in ans_set:
                return
            ans_set.add(n)
            if rooms[n]:
                for i in rooms[n]:
                    dfs(i)
        dfs(0)
        return True if len(ans_set) == room_cnt else False
