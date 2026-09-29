class HashTable:
    def __init__(self, capacity=15):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

    def put(self, key, value):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, val) in enumerate(bucket):
            if key == k:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > 0.75:
            self._resize()
    
    def get(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for k, val in bucket:
            if key == k:
                return val
        return None
    
    def remove(self, key):
        index = self._hash(key)
        bucket = self.table[index]
        for i, (k, val) in enumerate(bucket):
            if key == k:
                bucket.pop(i)
                self.size -= 1
                return True
        return False
    
    def contians(self, key):
        index = self._hash(key)
        bucket = self.table(index)
        for k, _ in enumerate(bucket):
            if key == k:
                return True
        return False

    def __len__(self):
        return self.size
    
    def __repr__(self):
        items = []
        for bucket in self.table:
            for key, value in bucket:
                items.append(f"{key}: {value}")
        return "{" + ", ".join(items) + "}"

def hash_table_operations(operations):
    # operations is a list of tuples:
    #   ("put", key, value)
    #   ("get", key)
    #   ("delete", key)
    # Return a list of results for every get and delete operation.
    ht = HashTable()
    ans = []
    for op in operations:
        if op[0] == "put":
            ht.put(op[1], op[2])
        elif op[0] == "get":
            ans.append(ht.get(op[1]))
        elif op[0] == "delete":
            ans.append(ht.remove(op[1]))
        else:
            pass
    return ans