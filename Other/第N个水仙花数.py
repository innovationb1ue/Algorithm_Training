
def solve(n, m):
    start = 10**(n-1)
    end = start * 10
    count = -1
    for num in range(start, end):
        str_num = str(num)
        charac_sum = 0
        for c in str_num:
            charac_sum += int(c) ** n
        if charac_sum == num:
            count += 1
        if count == m:
            return num


if __name__ == '__main__':
    p1, p2 = 3, 0
    res = solve(p1, p2)
    print(res)
