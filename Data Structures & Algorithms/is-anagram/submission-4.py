class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ansDict = {}
        for ch in s:
            if ch not in ansDict:
                ansDict[ch] = 1
            else:
                ansDict[ch] += 1
        for ch in t:
            if ch not in ansDict:
                return False
            ansDict[ch] -= 1
            if ansDict[ch] < 0:
                return False
        return True
        