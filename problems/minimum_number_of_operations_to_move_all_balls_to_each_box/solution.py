class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        a = [0]*len(boxes)

        counter = [0, 0]
        for i in range(len(boxes)):
            a[i] += sum(counter)
            counter[0] = sum(counter)
            if(boxes[i] == '1'):
                counter[1] += 1

        counter = [0, 0]

        for i in range(len(boxes)-1, -1, -1): 
            a[i] += sum(counter)
            counter[0] = sum(counter)
            if(boxes[i] == '1'):
                counter[1] += 1

        return a