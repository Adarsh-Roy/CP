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
    a, b = inintlist()
    if (a + b) % 3 == 0 and a <= 2 * b and b <= 2 * a:
        print("YES")
    else:
        print("NO")
