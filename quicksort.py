import random
def partition(arr, head, tail):
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
    if end - start <= 0:
        return
    mid = partition(arr, start, end)
    # quickSort two parts of the arr
    quickSort(arr, start, mid-1)
    quickSort(arr, mid+1, end)



arr = [10, 7, 8, 6, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n-1)
print("排序后的数组:")
for i in range(n):
    print("%d" % arr[i]),