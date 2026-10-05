class MinHeap:
    def __init__(self):
        self.heap = []
    
    def __len__(self):
        return len(self.heap)

    def empty(self):
        return len(self.heap) == 0
    
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def push(self, val):
        self.heap.append(val)
        self._heapifyUp(len(self.heap) - 1)
    
    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapifyDown(0)
        return root
    
    def _heapifyUp(self, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if self.heap[parent] > self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break
        
    def _heapifyDown(self, idx):
        n = len(self.heap)
        while True:
            smallest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            idx = smallest
        
def top_three_largest(values):
    # values: list of numbers
    # return the three largest values in descending order
    topK = MinHeap()
    for val in values:
        if len(topK) < 3:
            topK.push(val)
        elif val > topK.peek():
            topK.pop()
            topK.push(val)
    result = []
    while not topK.empty():
        result.append(topK.pop())
    return result[::-1]