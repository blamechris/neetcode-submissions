class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggestNum = max(arr)
        i = 0
        while i < len(arr)-1:
            if arr[i] < biggestNum:
                arr[i] = biggestNum
                i+=1
            elif arr[i] > biggestNum:
                i+=1 
            else:
                biggestNum = max(arr[i+1:])
                arr[i] = biggestNum
                i+=1
                continue

        arr[-1] = -1
        return arr