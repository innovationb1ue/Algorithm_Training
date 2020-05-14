class MonoStack:
    def __init__(self):
        self.stack = []

    @staticmethod
    def next_greater_number(nums:list) -> list:
        stack = []  # element in stack will be from small to large
        ans = []
        # reverse order to go through the nums
        for i in range(len(nums)-1, -1, -1):
            cur = nums[i]
            # check for the next num that num > cur
            while stack != [] and stack[-1] <= cur:
                # pop it if the num in stack < cur
                stack.pop()
            # make answer
            ans.append(-1 if stack == [] else stack[-1])
            # push current num into the stack to be checked later
            stack.append(cur)
        # reverse because stack top is in tail of list before reverse
        return ans[::-1]

    @staticmethod
    def next_greater_number_index(nums: list) -> list:
        stack = []  # element in stack will be from small to large
        # store index in ans
        ans = []
        # reverse order to go through the nums
        for i in range(len(nums) - 1, -1, -1):
            cur = nums[i]
            # check for the next num that num > cur
            while stack != [] and nums[stack[-1]] <= cur:
                # pop it if the num in stack < cur
                stack.pop()
            # make answer
            ans.append(0 if stack == [] else stack[-1] - i)
            # push cur index into the stack to be checked later
            stack.append(i)
        return ans

    @staticmethod
    def next_greater_number_index_rounded(nums: list) -> list:
        stack = []  # element in stack will be from small to large
        # store index in ans
        n = len(nums)
        ans = [0] * n
        # reverse order to go through the nums
        for i in range(2*n - 1, -1, -1):
            cur = nums[i % n]
            # check for the next num that num > cur
            while stack != [] and nums[stack[-1]] <= cur:
                # pop it if the num in stack < cur
                stack.pop()
            # make answer
            ans[i % n] = 0 if stack == [] else stack[-1] - i
            # push cur index into the stack to be checked later
            stack.append(i % n)
        return ans


if __name__ == '__main__':
    e = MonoStack()
    e.next_greater_number_index([1, 2, 6])
    r2 = e.next_greater_number_index_rounded([1, 9, 2, 6])
    print(r2)