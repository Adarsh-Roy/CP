t = int(input())


def f(n, m) -> int:
    if n <= 3 and m <= 3:
        return min(n, m)
    if n > m:
        n_left = n % 3
        return f(n_left, m) + m * (n // 3)
    else:
        m_left = m % 3
        return f(n, m_left) + n * (m // 3)


for i in range(t):
    n, m = map(int, input().split())
    print(f(m, n))
