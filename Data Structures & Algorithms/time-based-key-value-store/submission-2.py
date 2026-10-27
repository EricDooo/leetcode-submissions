class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) # (val, timestamp)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])
    
    def get(self, key: str, timestamp: int) -> str:
        tstamps = self.store[key]
        res = ""
        l, r = 0, len(tstamps) - 1

        while l <= r:
            m = (l+r)//2
            if tstamps[m][1] <= timestamp:
                res = tstamps[m][0]
                l = m + 1
            else:
                r = m - 1
            
        return res