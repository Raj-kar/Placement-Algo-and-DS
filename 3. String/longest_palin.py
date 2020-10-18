def lengthOfLongestSubstring(s: str) -> int:
    d = ""
    f = ""
    for i in range(len(s)):  # i = 4, i < 5
        if s[i] not in f:   # c not in f -> False
            f += s[i]       # f = "bac"
        else:
            if len(d) < len(f):  # 3 < 3
                d = f           # d = ba
            f = f[f.index(s[i])+1:] + s[i]   #

    return max(len(d), len(f))


print(lengthOfLongestSubstring("babac"))
