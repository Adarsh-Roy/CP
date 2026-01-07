import sys
from collections import Counter

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

n = len(s)

c = Counter(s)
left = ""
middle = ""
odd_mila = False
for x, f in c.items():
    if f & 1:
        if odd_mila or n & 1 == 0:
            print("NO SOLUTION")
            exit()
        else:
            odd_mila = True
            middle = x * f
    else:
        left += x * (f // 2)

if n & 1:
    print(left + middle + left[::-1])
else:
    print(left + left[::-1])
