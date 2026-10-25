class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append((value, timestamp))
        # The values are a list of tuples including time stamp and values

    def get(self, key: str, timestamp: int) -> str:
        val = self.timeMap.get(key, [])
        l, r = 0, len(val)-1
        res = "" 
        while l <= r:
            m = (l+r)//2 
            if val[m][1] <= timestamp:
                res = val[m][0]
                l = m+1 
            else:
                r=m-1
        return res 
