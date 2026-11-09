class Solution:
    def trap(self, height: List[int]) -> int:
        m=0
        num=0
        total=0
        for i in range(len(height)):
            if height[i]>num:
                m=i
                num=height[i]
        running_max=0
        for i in range(m):
            if height[i]>running_max:
                running_max=height[i]
            total+=running_max-height[i]
        running_max=0
        for i in range(len(height)-1,m,-1):
            if height[i]>running_max:
                running_max=height[i]
            total+=running_max-height[i]
        return total
