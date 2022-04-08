import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.lists,self.num = [],k
        for i in nums:
            self.add(i)

    def add(self, val: int) -> int:
        heapq.heappush(self.lists, val)
        if len(self.lists) > self.num: 
            # Pop and return the smallest item from the heap
            heapq.heappop(self.lists)
        return self.lists[0]

