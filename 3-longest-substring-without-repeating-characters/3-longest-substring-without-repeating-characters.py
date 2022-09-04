class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        
        mp = {}
        i = 0
        
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1
            
        return ans