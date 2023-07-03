class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:

        if s == goal:
            if len(set(s)) < len(goal):
                return True
            else:
                return False

        for i in range(len(s)):
            if s[i] != goal[i]:
                for j in range(len(goal)-1,i,-1):
                    if s[i] == goal[j]:
                        s = s[0:i]+s[j] +s[i+1:j]+s[i]+s[j+1:]
                        if s == goal:
                            return True
                        else:
                            return False
