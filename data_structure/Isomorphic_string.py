class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict_correspond_s = {}
        dict_correspond_t = {}
        for i in range(len(s)):#the same length
            if s[i] not in dict_correspond_s and t[i] not in dict_correspond_t:
                dict_correspond_s[s[i]] = t[i]
                dict_correspond_t[t[i]] = s[i]
            elif s[i] in dict_correspond_s and t[i] in dict_correspond_t:
                if dict_correspond_s[s[i]] != t[i] or dict_correspond_t[t[i]] != s[i]:
                    return False
            else:
                return False
        return True
