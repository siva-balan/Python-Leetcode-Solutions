class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        out = ""
        for i in s:
            if i.isalnum():
                out += i
        out = out.lower()
        rev = out[::-1]

        if out == rev:
            return True
        else:
            return False
