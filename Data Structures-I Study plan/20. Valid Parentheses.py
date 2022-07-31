class Solution:
    def isValid(self, s: str) -> bool:
            stack=[]
            for i in s:
                if i in ["(","[","{"]:
                    stack.append(i)
                elif len(stack) !=0 and i==")" and stack[-1]=="(":
                    stack.pop()
                elif len(stack) !=0 and i=="]" and stack[-1]=="[":
                    stack.pop()
                elif len(stack) !=0 and i=="}" and stack[-1]=="{":
                    stack.pop()
                
                else:
                    return False
            return stack == []
