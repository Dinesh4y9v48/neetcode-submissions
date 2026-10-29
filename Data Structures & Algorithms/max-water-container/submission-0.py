class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_water = 0

        while left < right:
            width = right - left
            h = min(heights[left], heights[right]) 
            area = width * h 

            max_water = max(max_water, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water


        # res = 0
        # l, r= 0,len(heights)-1

        # while l<r:
        #     area = (r-l) * min(heights[l], heights[r])
        #     res = max(res, area)

        #     if heights[l] < heights[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return res
          

