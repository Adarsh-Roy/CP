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


from itertools import groupby


def runs(stri):
    return [(ch, sum(1 for _ in group)) for ch, group in groupby(stri)]


t = inint()
for _ in range(t):
    p = instr()
    s = instr()
    rp, rs = runs(p), runs(s)
    ok = len(rp) == len(rs) and all(
        cp == cs and lp <= ls <= 2 * lp for (cp, lp), (cs, ls) in zip(rp, rs)
    )
    print("YES" if ok else "NO")
