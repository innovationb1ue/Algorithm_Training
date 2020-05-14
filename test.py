N, L = [int(i) for i in input().split()]
print(N, L)
ans = []
# i为项数
for i in range(L, 101):
    # 如果能找到一个整数的a1
    if (2*N + i - i**2) % (2*i) == 0:
        # a1
        start = (2*N + i - i**2) // (2*i)
        if start < 0:
            print('No')
            exit()
        ans = [str(i) for i in range(start, start + i)]
        print(' '.join(ans))
        exit()
print('No')
