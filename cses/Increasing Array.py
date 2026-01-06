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
ans = 0
cur = ns[0]
for n in ns[1:]:
    if n < cur:
        ans += cur - n
    else:
        cur = n
print(ans)
