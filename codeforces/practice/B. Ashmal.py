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
    n = inint()
    s = ""
    aa = instrlist()
    for a in aa:
        if (s + a) < (a + s):
            s = s + a
        else:
            s = a + s
    print(s)
