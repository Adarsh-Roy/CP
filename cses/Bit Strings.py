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


MOD = 1000_000_007
n = inint()
s = 1
for i in range(n):
    s <<= 1
    s %= MOD
print(s)
