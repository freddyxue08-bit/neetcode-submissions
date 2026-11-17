class TimeMap:

    def __init__(self):
        self.names={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.names.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        s = self.names.get(key, [])
        l, r = 0, len(s) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            if s[m][0] <= timestamp:
                res = s[m][1]      # valid candidate; look for a later one
                l = m + 1
            else:
                r = m - 1          # too late
        return res