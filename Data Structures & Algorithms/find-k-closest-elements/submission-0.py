class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # We get a hashmap (to keep track of freq.) and store the values that appear and the amount of times. Then we can 
        # We take a hashmap with abs. differences as the key and a list of integers (ideally sorted) as the value. Since arr is sorted we know whatever is seen first will be in order, ergo we can do this in O(n) with O(n) space. With the hashmap we just iterate through the keys in order (for i in range(0,n)) and we go until we have grabbed k elements

        diff = defaultdict(list)
        for n in arr:
            diff[abs(n-x)].append(n)
        
        res = []
        i = 0
        while k:
            for n in diff[i]:
                if k <= 0: break
                res.append(n)
                k-=1 
            i+=1 
        res.sort()
        return res
            
        