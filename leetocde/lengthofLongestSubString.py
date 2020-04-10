def lengthofLongestSubstring(s):
    """
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    substrings = []
    for i in range(len(s)):
        temp = ""
        for j in s[i+1:]:
            if j==s[i] or j in temp:
                print(s[i]+temp)
                substrings.append(len(s[i]+temp))
                break
            temp+=j
        print(s[i]+temp)
        substrings.append(len(s[i]+temp))
     if substrings:
            return max(substrings)
     else:
         return 0

print(lengthofLongestSubstring("abcabcbb"))
