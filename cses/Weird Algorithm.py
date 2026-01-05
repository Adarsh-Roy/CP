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
s = str(n)
while n != 1:
    if n & 1:
        n = 3 * n + 1
    else:
        n = n // 2
    s += " " + str(n)
print(s)
