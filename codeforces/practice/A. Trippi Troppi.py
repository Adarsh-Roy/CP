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
for _ in range(t):
    names = instrlist()
    modern = [name[0] for name in names]
    print("".join(modern))
