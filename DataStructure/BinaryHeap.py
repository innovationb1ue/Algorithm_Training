class BinaryHeap:
    def __init__(self):
        self.array = [-1]  # index 0 is not used !
        self.N = 0

    def get_all(self):
        return self.array

    def bmax(self):
        return self.array[1]

    def parent(self, k:int):
        # return index of parent
        return k//2

    def insert(self, element:int):
        self.N += 1
        self.array.append(element)
        self.swim(self.N)

    def delMax(self):
        self.array[1], self.array[-1] = self.array[-1], self.array[1]
        self.swim(self.N)

    def exchange(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def swim(self, k:int):
        while k > 1 and self.array[k] > self.array[self.parent(k)]:
            self.exchange(k, self.parent(k))
            k = self.parent(k)

    def sink(self, k:int):
        # find largest child
        if older:=self.left(k) >= len(self.array):
            return
        if right := self.right(k) < len(self.array):
            if self.array[right] > self.array[older]:
                older = right
        # sinking
        while k < self.N and self.array[k] < self.array[older]:
            self.exchange(k, older)


    def left(self, k:int):
        return k*2

    def right(self, k:int):
        return k*2+1

