class QueueNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return f'({self.key}: {self.value})'

class Cache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.back = None
        self.front = None
        self.memo = {}

    def __getitem__(self, key):
        value = self.memo[key].value
        self._update(key, value)
        return value

    def __setitem__(self, key, value):
        if key in self.memo:
            self._update(key, value)
            return
        
        self.memo[key] = new = QueueNode(key, value)
        self._push(new)

        if self.full:
            self._pop()

    def _update(self, key, new_value):
        node = self.memo[key]
        node.value = new_value
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        self._push(node)

    def _push(self, node):
        if self.back:
            node.next = self.back
            self.back.prev = node
        if not self.front:
            self.front = node

        self.back = node

    def _pop(self):
        last = self.front
        self.front = last.prev
        self.front.next = None
        del self.memo[last.key]

    @classmethod
    def memoize(cls, size):
        return cls(size)

    @property
    def full(self):
        return len(self.memo.keys()) >= self.max_size

    def __str__(self):
        if not self.back:
            return 'Empty'
        
        current = self.back
        self._names = [str(current)]
        while (current.next != None):
            current = current.next
            self._names.append(str(current))
        
        return f"in -> {' <-> '.join(self._names)} -> out" 
         

if __name__ == '__main__':
    cache = Cache.memoize(3)
    cache[1] = 'I'
    cache[2] = 'Love'
    cache[3] = 'You'
    cache[4] = 'So'
    cache[5] = 'Much'
    cache[3] = 'fermat'
    cache[10] = 'new'


    print(cache)
    cache._pop()
    print(cache)
    new = QueueNode(1000, 'hi')
    cache._push(new)
    print(cache)
    print(cache[5])
    print(cache)
