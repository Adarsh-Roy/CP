import sys
import math

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
for k in range(1, n + 1):
    if k == 1:
        print(0)
        continue
    total = math.comb(k * k, 2)
    attack = (k - 1) * (k - 2) * 2 * 2 if k > 2 else 0
    print(total - attack)
