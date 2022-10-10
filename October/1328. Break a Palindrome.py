class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        n =len(palindrome)
        if n == 1:
            return ""        
        
        for i in range(n//2):
            if palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                return palindrome
        return palindrome[:n-1] + "b"
