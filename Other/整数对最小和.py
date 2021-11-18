"""����������������array1 array2  ����Ԫ�ذ��������� �����arr1 arr2�зֱ�ȡ��һ��Ԫ�أ��ɹ���һ��Ԫ��
     ������Ҫȡ��k��Ԫ�أ�����ȡ��������Ԫ����ͼ���͵���Сֵ
     ע�⣺����Ԫ�ض�Ӧarr1 arr2���±�����ͬ�� ��Ϊͬһ��Ԫ��
 ��������
        ������������arr1 arr2
        ÿ���׸�����Ϊ�����Сsize   0<size<=100
        arr1��2�е�ÿ��Ԫ��   0< <1000
        ������һ��  ������k   0<k<=arr1.size * arr2.size
     �������
       ����Ҫ�����Сֵ
     ����
    ����
       3 1 1 2
       3 1 2 3
    ���
       4
    ˵������������Ҫȡ����Ԫ�أ�
     ȡ��һ�������0��Ԫ����ڶ��������0��Ԫ�����һ��Ԫ��
     [1,1]
    ȡ��һ�������1��Ԫ����ڶ��������0��Ԫ�����һ��Ԫ��
     [1,1]
    ���Ϊ1+1+1+1=4 ,����Ҫ����С"""



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