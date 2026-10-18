class TimeMap:

    def __init__(self):
        self.hm = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if self.hm.get(key):
            # Since we are adding it in order we just need to look until there is a timestamp greater than the current one and insert before then. 
        #    values = self.hm[key]
        #    for i in range(len(values)):
        #        if values[i][1] >= timestamp:
        #            self.hm[key].insert(i, (value, timestamp))
        #            return None
        #   self.hm[key].append((value, timestamp))
        #else:
        #    self.hm[key] = self.hm.get(key, [(value, timestamp)])

        if key not in self.hm:
            self.hm[key] = []
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # we have a sorted list so we can binary search 
        values = self.hm.get(key, [])
        l, r = 0, len(values)-1
        res = "" 
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m+1
            else:
                r = m - 1
        return res 

        
