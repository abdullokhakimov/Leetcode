class Solution:
    # 1.Solution
    def maxAreaBruteForce(self, heights):
        res = 0
        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res

    # 2.Solution
    def maxAreaTwoPointers(self, height):
        output = 0
        l, r = 0, len(height) - 1
        while l != r:
            area = (r - l) * min(height[l], height[r])
            if area > output:
                output = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return output

height = [1,8,6,2,5,4,8,3,7]
print(Solution.maxAreaTwoPointers(height))
# 49

'''
EXPLANATION:
 
1.Solution: Brute Froce O(n^2)
We use a nested loop: 
The outer loop iterates through each index i of the list, and the inner loop iterates from the next index j onward. 
For each pair (i, j), it calculates the area between the lines at those indices by taking the smaller of the two heights and multiplying it by the distance between the indices, which is j - i. 
If this area is greater than the current value of output, it updates output with this new value. 
After checking all pairs, it returns the maximum area stored in res.

2.Solution: Two Pointers O(n)
It starts with two pointers, l at the beginning and r at the end of the list height. 
In each iteration of the while loop, it calculates the area formed between the two lines pointed to by l and r, using the shorter of the two heights and the distance between them. 
If this area is greater than the current maximum output, it updates output. Then, instead of checking all pairs, it moves the pointer corresponding to the shorter line inward, because moving the taller line cannot increase the area. 
This process continues until the two pointers meet, ensuring an optimal solution in linear time.
'''