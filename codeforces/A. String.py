t = int(input())  # Number of test cases

for _ in range(t):
    s = input().strip()  # Read the binary string
    print(s.count("1"))  # Count and print the number of '1's
