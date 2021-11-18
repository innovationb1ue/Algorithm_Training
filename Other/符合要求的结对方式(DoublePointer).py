from collections import defaultdict

"""
两两配对结成工作小组，满足sum = target
"""

def solve(n, arr, target):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                count += 1
    return count


if __name__ == '__main__':
    n = 5
    array = [1, 2, 2, 2, 3]
    target = 4
    res = solve(n, array, target)
    print(res)