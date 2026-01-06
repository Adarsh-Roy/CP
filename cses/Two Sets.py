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
S = n * (n + 1) // 2
if S & 1:
    print("NO")
else:
    print("YES")
    target = S // 2
    a = set()
    b = set()
    for i in range(n, 0, -1):
        if i <= target:
            a.add(str(i))
            target -= i
        else:
            b.add(str(i))
    print(len(a))
    print(" ".join(a))
    print(len(b))
    print(" ".join(b))
