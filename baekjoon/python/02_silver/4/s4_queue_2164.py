"""
silver4 2164
카드2
"""

from collections import deque
import sys

N = int(sys.stdin.readline())

cards = deque([i+1 for i in range(N)])

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())

print(cards[0])
