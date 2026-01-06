import sys

n = int(sys.stdin.readline())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    nums = []
    for i in range(2, n + 1, 2):
        nums.append(str(i))
    for i in range(1, n + 1, 2):
        nums.append(str(i))
    sys.stdout.write(" ".join(nums))
