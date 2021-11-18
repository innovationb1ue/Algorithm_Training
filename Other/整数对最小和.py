"""给定两个整数数组array1 array2  数组元素按升序排列 假设从arr1 arr2中分别取出一个元素，可构成一对元素
     现在需要取出k对元素，并对取出的所有元素求和计算和的最小值
     注意：两对元素对应arr1 arr2的下标是相同的 视为同一对元素
 输入描述
        输入两行数组arr1 arr2
        每行首个数字为数组大小size   0<size<=100
        arr1，2中的每个元素   0< <1000
        接下来一行  正整数k   0<k<=arr1.size * arr2.size
     输出描述
       满足要求的最小值
     例子
    输入
       3 1 1 2
       3 1 2 3
    输出
       4
    说明：用例中需要取两个元素，
     取第一个数组第0个元素与第二个数组第0个元素组成一个元素
     [1,1]
    取第一个数组第1个元素与第二个数组第0个元素组成一个元素
     [1,1]
    求和为1+1+1+1=4 ,满足要求最小"""



def solve(arr1, arr2, n):
    """
    Time complexity O(n)
    Space O(1) only constants

    """
    if n == 0:
        return 0
    max_index1 = arr1[0]
    max_index2 = arr2[0]
    arr1 = arr1[1:]
    arr2 = arr2[1:]
    p1, p2 = 0, 0
    res = [arr1[0] + arr2[0]]
    while len(res) < n:
        if p1 == max_index1 - 1 and p2 == max_index2 - 1:
            raise ValueError()
        if p1 == max_index1 - 1:
            p2 += 1
        elif p2 == max_index1 - 1:
            p1 += 1
        else:
            if arr1[p1+1] - arr1[p1] <= arr2[p2+1] - arr2[p2]:
                p1 += 1
            else:
                p2 += 1
        res.append(arr1[p1] + arr2[p2])

    return sum(res)


if __name__ == '__main__':
    arr1 = [3, 1, 1, 2]
    arr2 = [3, 1 ,2 ,3]
    param3 = 3
    res = solve(arr1, arr2, param3)
    print(res)