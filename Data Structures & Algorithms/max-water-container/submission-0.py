class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        area=0
        while j>i:
            height=min(heights[i],heights[j])
            width=j-i
            if height*width>area:
                area=height*width
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return area