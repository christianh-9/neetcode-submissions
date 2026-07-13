class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = dict()
        t_seen = dict()

        for char in s:
            if char in s_seen:
                s_seen[char] +=1
            else:
                s_seen[char] = 1
        
        for char in t:
            if char in t_seen:
                t_seen[char] +=1
            else:
                t_seen[char] = 1
        
        if s_seen == t_seen:
            return True
        else:
            return False