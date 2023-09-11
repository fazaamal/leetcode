class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        chars = [None] * len(indices)
        for char, i in zip(list(s), indices):
            chars[i] = char

        return ''.join(chars)
            