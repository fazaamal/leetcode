class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
            # if(sorted_word not in d):
            #     d[sorted_word] = []
            # d[sorted_word].append(word)
        
        return list(anagram_map.values())
        # return list(d.values())