t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    arr = arr[::-1]
    total = 0
    for i in range(n):
        fg = arr[i] - i
        if fg > 0:
            total += fg
        else:
            break
    ans = total % 1000000007
    print(ans)
    t -= 1