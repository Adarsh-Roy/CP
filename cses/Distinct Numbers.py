import sys

input = sys.stdin.readline


def inint() -> int:
    return int(input())


def instr() -> str:
    return input().strip()


def inintlist() -> list[int]:
    return list(map(int, input().split()))


def instrlist() -> list[str]:
    return input().split()


n = inint()
ns = inintlist()
ns.sort()
ans = 1
last = ns[0]
for cur in ns[1:]:
    if last == cur:
        continue
    else:
        last = cur
        ans += 1
print(ans)
