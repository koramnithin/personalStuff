class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        s = list(s)
        n = len(s)-1
        v = ['a','e','i','o','u','A','E','I','O','U']
        j = n
        while(i<j):
            if(s[i] in v):
                if(s[j] in v):
                    temp = s[i]
                    s[i] = s[j]
                    s[j] = temp
                    j -= 1
                else:
                    j -= 1
                    continue
            i += 1
        return ''.join(s)
s = Solution()
print(s.reverseVowels('leetcode'))