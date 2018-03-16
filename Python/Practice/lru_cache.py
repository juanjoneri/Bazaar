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

        if self.too_big:
            self._pop()

    def _update(self, key, new_value):
        node = self.memo[key]
        node.value = new_value
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev:
            # node is front
            self.front = node.prev
            self.front.next = None
        else:
            # node is back
            return
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
    def memoize(cls, max):
        def decorator(fun):
            cache = cls(max)
            def wrapper(*args):
                if args not in cache.memo:
                    cache[args] = fun(*args)
                    print(cache)
                return cache[args]
            return wrapper
        return decorator

    @property
    def too_big(self):
        return len(self.memo.keys()) > self.max_size

    def __str__(self):
        if not self.back:
            return 'Empty'
        
        current = self.back
        self._names = [str(current)]
        while (current.next != None):
            current = current.next
            self._names.append(str(current))
        
        return f"in -> {' <-> '.join(self._names)} -> out" 

@Cache.memoize(max = 3)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    
    print(fib(6))


