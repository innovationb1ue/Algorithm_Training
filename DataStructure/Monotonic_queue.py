class MonoQueue:
    def __init__(self):
        # queue is monotonic decreasing
        self.queue = []

    @property
    def head(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    @property
    def tail(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def max(self):
        return self.head

    def popback(self):
        if self.queue:
            return self.queue.pop()

    def __pushback(self, x: int):
        self.queue.append(x)

    def push(self, x: int):
        while self.queue and self.tail < x:
            self.popback()
        self.__pushback(x)

    def pop(self, x: int):
        # note here
        if self.queue and self.head == x:
            return self.queue.pop(0)


def SolutionSlideWindow(nums: list, k: int) -> list:
    window = MonoQueue()
    res = []
    for i in range(k-1):
        window.push(nums[i])
    for i in range(k-1, len(nums)):
        # push in the next element
        window.push(nums[i])
        # get the maximum in window
        res.append(window.max())
        # pop one to spare space for next loop
        window.pop(nums[i-k+1])
    return res

if __name__ == '__main__':
    res = SolutionSlideWindow([1,3,-1,-3,5,3,6,7], 3)
    print(res)


