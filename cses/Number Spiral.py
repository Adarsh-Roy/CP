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


t = inint()

for i in range(t):
    y, x = inintlist()
    if y < x:
        if x & 1:
            print(x * x - y + 1)
        else:
            print((x - 1) * (x - 1) + y)

    else:
        if y & 1:
            print((y - 1) * (y - 1) + x)
        else:
            print(y * y - x + 1)
