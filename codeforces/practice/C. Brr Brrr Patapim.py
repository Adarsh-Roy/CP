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
    n = inint()
    grid = []
    for _ in range(n):
        grid.append(inintlist())
    ans = [None] * 2 * n
    remaining = set((n + 1 for n in range(2 * n)))
    for i in range(n):
        ans[i + 1] = grid[0][i]
        remaining.remove(grid[0][i])
        ans[2 * n - i - 1] = grid[n - 1][n - i - 1]
        if i != n - 1:
            remaining.remove(grid[n - 1][n - i - 1])
    ans[0] = remaining.pop()
    print(*ans)
