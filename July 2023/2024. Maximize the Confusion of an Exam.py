class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        output = i = 0
        char_count = collections.Counter()

        for j in range(len(answerKey)):

            char_count[answerKey[j]] += 1
            output = max(output, char_count[answerKey[j]])

            if j - i + 1 > output + k:
                char_count[answerKey[i]] -= 1
                i += 1

        return len(answerKey) - i
