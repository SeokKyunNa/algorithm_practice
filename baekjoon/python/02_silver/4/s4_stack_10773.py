"""
silver4 10773
제로
"""

import sys

K = int(sys.stdin.readline())
account = []

for _ in range(K):
    num = int(sys.stdin.readline())
    if num == 0:
        account.pop()
    else:
        account.append(num)

print(sum(account))


