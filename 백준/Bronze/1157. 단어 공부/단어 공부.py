import sys
from collections import Counter

S = str(sys.stdin.readline().strip())

counter = Counter(S.upper())

max_count = [char for char,cnt in counter.items() if cnt == max(counter.values())]

if len(max_count) > 1:
    print("?")
else:
    print("".join(max_count))