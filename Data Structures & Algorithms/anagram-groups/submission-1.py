class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapped : dict[str, list[str]] = {}

        for st in strs:

            sorted_str = sorted(st)
            sorted_str = "".join(sorted_str)
            if sorted_str in mapped:
                mapped[sorted_str].append(st)
            else:
                mapped[sorted_str] = [st]
        
        return list(mapped.values())