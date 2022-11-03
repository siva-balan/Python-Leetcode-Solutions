class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
    
        """output = 0
        s = 0
        seen = set()
        for i in words:
            x = words.count(i)
            if i[0] == i[1]:
                if x%2 == 0 and i not in seen:
                    output += x
                    seen.add(i)
                elif x%2 ==1 and i not in seen:
                    output += x-1
                    seen.add(i)
                    s =1
            elif i[0] < i[1]:
                y = i[1] + i[0]
                output += 2 *min(x,words.count(y))
        if s ==1:
            output += 1
        return output*2"""
        
        
        count = Counter(words)
        answer = 0
        central = False
        for word, count_of_the_word in count.items():
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    central = True
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer
