import random


def partition(arr, head, tail):
    """Left side pivot all smaller, right side pivot all larger"""
    # randomly select a pivot
    pivot = random.randint(head, tail)
    # switch pivot to last item
    arr[pivot], arr[tail] = arr[tail], arr[pivot]
    # move left pointer to pre location
    i = head - 1
    # go through the whole arr
    for j in range(head, tail):
        # if num < pivot, switch it with the left pointer
        if arr[j] < arr[tail]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # move i to the mid position (next position)
    i += 1
    # switch pivot back to mid postition
    arr[i], arr[tail] = arr[tail], arr[i]
    return i


def quickSort(arr, start, end):
    """sort for interval [start, end]"""
    if end - start <= 0:
        return
    mid = partition(arr, start, end)
    # quickSort two parts of the arr
    quickSort(arr, start, mid-1)
    quickSort(arr, mid+1, end)



arr = [1332802,1177178,1514891,871248,753214,123866,1615405,328656,1540395,968891,1884022,252932,1034406,1455178,821713,486232,860175,1896237,852300,566715,1285209,1845742,883142,259266,520911,1844960,218188,1528217,332380,261485,1111670,16920,1249664,1199799,1959818,1546744,1904944,51047,1176397,190970,48715,349690,673887,1648782,1010556,1165786,937247,986578,798663]
n = len(arr)
quickSort(arr, 0, n-1)
print("排序后的数组:")
print(arr)
print(arr[-24])