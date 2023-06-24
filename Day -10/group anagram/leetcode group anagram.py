class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in table:
                table[sorted_string] = []

            table[sorted_string].append(string)
        return list(table.values())
