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
        
class MaxHeap:
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
            if self.heap[parent] < self.heap[idx]:
                self.heap[parent], self.heap[idx] = self.heap[idx], self.heap[parent]
                idx = parent
            else:
                break
        
    def _heapifyDown(self, idx):
        n = len(self.heap)
        while True:
            largest = idx
            left = 2 * idx + 1
            right = 2 * idx + 2
            if left < n and self.heap[left] > self.heap[largest]:
                largest = left
            if right < n and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == idx:
                break
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            idx = largest

def running_median(stream):
    # stream: list of numbers arriving one at a time
    # return a list of medians after each insertion
    medians = []
    max_heap, min_heap = MaxHeap(), MinHeap()
    for val in stream:
        if max_heap.empty() or val <= max_heap.peek():
            max_heap.push(val)
        else:
            min_heap.push(val)

        if len(max_heap) > len(min_heap) + 1:
            min_heap.push(max_heap.pop())
        elif len(max_heap) < len(min_heap):
            max_heap.push(min_heap.pop())
        
        if len(max_heap) == len(min_heap):
            medians.append((max_heap.peek() + min_heap.peek()) / 2.0)
        else:
            medians.append(max_heap.peek())
    return medians