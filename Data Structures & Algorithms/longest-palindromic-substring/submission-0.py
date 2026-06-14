class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, max_len = 0, 1

        def expand(l: int, r: int) -> None:
            nonlocal start, max_len
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur = r - l + 1
                if cur > max_len:
                    start, max_len = l, cur
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)       # odd length
            expand(i, i + 1)   # even length
        print(s[start:start + max_len], start, max_len)
        return s[start:start + max_len]
