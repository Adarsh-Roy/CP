t = int(input())  # Read the number of testcases

for _ in range(t):
    n, k = list(map(int, input().split()))
    x = list(map(int, input().split()))
    count = {}
    ans = 0
    for i in x:
        comp_count = count.get(k - i, 0)
        if comp_count > 0:
            count[k - i] -= 1
            ans += 1
        else:
            count[i] = count.get(i, 0) + 1
    print(ans)
