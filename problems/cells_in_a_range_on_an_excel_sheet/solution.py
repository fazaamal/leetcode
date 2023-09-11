class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        cells = []

        for i in range(alpha.index(s[0]), alpha.index(s[3])+1):
            for q in range(int(s[1]), int(s[4])+1):
                cells.append(f'{alpha[i]}{q}')

        return cells