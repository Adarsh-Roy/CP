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


s = instr()
if not s:
    print(0)
else:
    maxi = 1
    cc = 1
    last = s[0]
    for c in s[1:]:
        if c == last:
            cc += 1
            maxi = max(cc, maxi)
        else:
            cc = 1
        last = c
    print(maxi)
