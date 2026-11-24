class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n and m:
            if nums2[n-1] > nums1[m-1]:
                nums1[n+m-1] = nums2[n-1]
                n-=1
            elif nums2[n-1] <= nums1[m-1]:
                nums1[m+n-1] = nums1[m-1]
                m-=1
        while n:
            nums1[n+m-1] = nums2[n-1]
            n-=1

         
        