class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1. Hashmap of values to index of nums1
        nums1Map = {}
        for i, v in enumerate(nums1):
            nums1Map[v] = i
        
        # 2. create res list
        res = [-1] * len(nums1)

        #3. loop through second loop to see if there is a next greater element 

        for i in range(len(nums2)):
            if nums2[i] in nums1Map:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        res[nums1Map[nums2[i]]] = nums2[j]
                        break 
        return res 

        
        