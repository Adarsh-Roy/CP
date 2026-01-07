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


n, x = inintlist()

ns = inintlist()
ns = [(ns[i], i) for i in range(len(ns))]

ns.sort()
i = 0
j = len(ns) - 1
while i < j:
    if ns[i][0] + ns[j][0] == x:
        print(f"{ns[i][1] + 1} {ns[j][1] + 1}")
        exit()
    elif ns[i][0] + ns[j][0] <= x:
        i += 1
    else:
        j -= 1

print("IMPOSSIBLE")
