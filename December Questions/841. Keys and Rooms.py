class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        n = len(rooms)
        
        visited = set()

        def seen(curr,visited):
            visited.add(curr)

            for i in rooms[curr]:
                if i not in visited:
                    seen(i,visited)

        seen(0,visited)

        if len(visited) == n:
            return True
        else:
            return False
