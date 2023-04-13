self.minheap=[]
        self.k=k
        self.nums=nums
        for i in self.nums:
            heapq.heappush(self.minheap,i)
            if len(self.minheap)>self.k:
                heapq.heappop(self.minheap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap,val)
        if len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0
