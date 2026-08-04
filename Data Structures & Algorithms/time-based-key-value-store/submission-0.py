class TimeMap:

    def __init__(self):
        self.table = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # create list for key if not there already
        if key not in self.table:
            self.table[key] = []
        # store timestamp value pair at the key
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # implement a binary search between timestamps to find faster
        low = 0
        if key in self.table:
            high = len(self.table[key]) - 1
        else: 
            return ""
        
        max = -1

        # return val at timestamp
        # if no val at timestamp, return the first one at a smaller time stamp than asked
        while low <= high:
            mid = (low + high) //2
            if self.table[key][mid][0] == timestamp:
                return self.table[key][mid][1]
            elif self.table[key][mid][0] < timestamp:
                max = mid
                low = mid+1
            else:
                high = mid - 1

        if max == -1:
            return ""

        # return the value part of the timestamp, value pair
        return self.table[key][max][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)