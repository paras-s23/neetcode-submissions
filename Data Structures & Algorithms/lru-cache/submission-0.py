class LRUCache:

    def __init__(self, capacity: int):
        self.lru = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.lru.keys():
            val = self.lru[key]
            del self.lru[key]
            self.lru[key] = val
            return val
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.lru:
            del self.lru[key]

        elif len(self.lru) == self.capacity:
            first_key = next(iter(self.lru))
            self.lru.pop(first_key)

        self.lru[key] = value

        
