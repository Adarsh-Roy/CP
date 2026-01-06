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
ans = 0
while n >= 5:
    n //= 5
    ans += n
print(ans)
