class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We can add nums2, at the end of nums1 so startingat m to end of the list. Then bubble sort O(n+n+m)
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i - m]
        ctr2 = 0 
        for i in range(len(nums1)):
            for j in range(0, len(nums1)-i-1):
                if nums1[j+1] < nums1[j]:
                    nums1[j+1], nums1[j] = nums1[j], nums1[j+1]
            
                