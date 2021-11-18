class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.pre = None
        self.next = None


class doubleList:
    def __init__(self):
        self.size = 0
        self._head = None
        self._tail = None

    def addFirst(self, x: Node) -> None:
        self.size += 1
        # check if the first element added to the list
        if self._head is None:
            self._head = x
            self._tail = x
        else:
            x.next = self._head
            self._head.pre = x
            self._head = x

    def removeLast(self) -> Node:
        if self.size <= 0:
            raise Exception('remove from empty list')
        if self.size == 1:
            self.size = 0
            temp = self._head
            self._head = None
            self._tail = None
            return temp
        elif self.size >= 2:
            temp = self._tail
            self._tail.pre.next = None
            self._tail = self._tail.pre
            self.size -= 1
            return temp

    def remove(self, x: Node):
        if x is None:
            return
        if self.size == 1:
            self._head = None
            self._tail = None
            self.size = 0
            return
        cur = self._head
        while cur:
            if cur == x:
                self.size -= 1
                # special case: first element
                if cur == self._head:
                    self._head = cur.next
                    self._head.pre = None
                # special case: last element
                elif cur == self._tail:
                    self._tail = self._tail.pre
                    self._tail.next = None
                # normal case: in the middle
                else:
                    cur.pre.next = cur.next
                    cur.next.pre = cur.pre
                break
            # move cur to next one
            cur = cur.next


class LRUcache:
    def __init__(self, cap: int):
        self.hashmap = {}
        self.cache = doubleList()
        self.cap = cap

    def get(self, k: int):
        if (res := self.hashmap.get(k)) is not None:
            self.put(k, res.val)
            return res.val
        else:
            return None

    def put(self, k: int, v: int):
        x = Node(k, v)
        # if already exist
        if self.hashmap.get(k) is not None:
            # delete old
            self.cache.remove(self.hashmap.get(k))
            # insert new
            self.cache.addFirst(x)
            # update map
            self.hashmap[k] = x
        else:
            # if cache is full
            if self.cache.size == self.cap:
                # delete the last cache
                last = self.cache.removeLast()
                # delete the map
                self.hashmap.pop(last.key)
            # insert new
            self.cache.addFirst(x)
            # update map
            self.hashmap[k] = x

if __name__ == '__main__':
    a = LRUcache(3)
    a.put(1, 2)
    a.put(3, 6)
    a.put(4, 8)
    a.put(5, 10)
    print(a.get(3))
    print(a.get(1))
    print(a.get(5))
