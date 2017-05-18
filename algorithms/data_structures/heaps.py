from copy import copy
from heapq import heappush, heappop, heappushpop


class MinHeap(object):
    def __init__(self, items=None, key=None):
        self.items = []
        self.key = key if key else lambda k: k

        for x in items or []:
            self.push(x)

    def _wrap(self, obj):
        """
        Wraps object in a tuple using the specified key for comparisons.
        """
        data = self.key(obj), obj
        return data

    def _unwrap(self, data):
        """
        Unwraps object tuple and returns the actual object that was added.
        """
        key, obj = data
        return obj

    def push(self, obj):
        """
        Pushes an object to the heap in O(log n) time.
        """
        heappush(self.items, self._wrap(obj))

    def pop(self):
        """
        Pops an object from the heap in O(log n) time.
        """
        return self._unwrap(heappop(self.items))

    def pushpop(self, obj):
        """
        A fast version of combining a push followed by a pop operation.
        """
        return self._unwrap(heappushpop(self.items, self._wrap(obj)))

    def peek(self):
        """
        Returns the root node of the heap without removing it in O(1) time.
        """
        if not self.items:
            return None
        return self._unwrap(self.items[0])

    def size(self):
        """
        Returns the size of the heap in O(1) time.
        """
        return len(self.items)

    def __len__(self):
        """
        Returns the size of the heap in O(1) time.
        """
        return self.size()

    def __iter__(self):
        """
        Returns a generator with the heap elements in order.
        """
        heap = self.__class__(key=self.key)
        heap.items = copy(self.items)
        while heap.size():
            yield heap.pop()


class MaxHeap(MinHeap):
    def _wrap(self, obj):
        return -self.key(obj), obj
