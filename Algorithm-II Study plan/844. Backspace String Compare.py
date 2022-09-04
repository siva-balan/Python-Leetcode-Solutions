class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for s1 in s:
            if s1 == '#' and s_stack:
                s_stack.pop()
                continue
            if s1 != '#': s_stack.append(s1)
        for t1 in t:
            if t1 == '#' and t_stack:
                t_stack.pop()
                continue
            if t1 != '#': t_stack.append(t1)
        return s_stack == t_stack
