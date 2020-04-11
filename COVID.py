t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().split()))
    l= []
    flag = 0
    for i in range(n):
        if arr[i] == 1:
            l.append(i)
    if len(l) > 1:
        for i in range(1,len(l)):
            if l[i] - l[i-1] < 6:
                flag = 1
                break
    if flag == 1:
        print("NO")
    else:
        print("YES")
    t -= 1