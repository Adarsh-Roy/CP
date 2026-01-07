import sys
import math

input = sys.stdin.readline
_ = input()
ns = list(map(int, input().split()))
ans, cur = ns[0], -math.inf
for n in ns:
    ans = max(ans, cur := max(cur + n, n))

print(ans)
