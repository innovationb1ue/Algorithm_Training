class Solution:
    def findKth(self, a: list[int], n: int, K: int) -> int:
        # write code here
        self.quick_sort(a, 0, len(a) - 1)
        return a[K - 1]

    def quick_sort(self, arr, start, end):
        """sort for [start, end]"""
        mid = self.partition(arr, start, end)
        self.partition(arr, start, mid - 1)
        self.partition(arr, mid + 1, end)

    def partition(self, arr, head, tail):
        pivot = head
        i = head - 1
        arr[pivot], arr[tail] = arr[tail], arr[pivot]
        for j in range(head, tail):
            if arr[j] < arr[tail]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        i += 1
        arr[tail], arr[i] = arr[i], arr[tail]
        return i

e = Solution()
res = e.findKth([1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663],49,24)
print(res)


