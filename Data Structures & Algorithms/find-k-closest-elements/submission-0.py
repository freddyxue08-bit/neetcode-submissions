class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a,b=0,k
        closest=[]
        for i in range(k):
            closest.append(arr[i])
        for i in range(len(arr)-k):
            if abs(arr[b]-x)<abs(arr[a]-x):
                closest.append(arr[b])
                closest.pop(0)
            b+=1
            a+=1
        return closest

        