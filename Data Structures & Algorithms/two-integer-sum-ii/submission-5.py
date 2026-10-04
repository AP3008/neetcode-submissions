class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # target = index1 + index2 && index1 < index2 && index1 != index2
        # index1 = target - index2
        # Hashmap sol
        #seen = defaultdict(int)
        #for i in range(len(numbers)):
         #   val = target - numbers[i]
          #  if seen[val]:
           #     return [seen[val], i+1]
            #seen[numbers[i]] = i+1
        #return []

        # binary search sol. 
        # For each number we want to binary search the target, if it dones't exist we move on. 

        for i in range(len(numbers)):
            val = target - numbers[i]
            l, r = i+1, len(numbers)-1
            while l <= r:
                m = l + (r-l) // 2
                if numbers[m] == val:
                    return [i+1, m+1]
                elif numbers[m] < val:
                    l = m + 1
                else:
                    r = m - 1
        return [] 

